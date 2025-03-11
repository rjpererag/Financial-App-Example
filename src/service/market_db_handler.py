from .db_handler import DBHandler
from ..settings.db_authentication import DBCredentials
from ..utils.market_value_schema import db_schema

from src.utils.logger import logger


class MarketDBHandler(DBHandler):

    def __init__(self, creds: DBCredentials) -> None:
        super().__init__(creds=creds)
        self.db_schema = db_schema

    def __validate_table(self, table_name: str, target: str) -> bool:
        if self.db_schema.get(table_name, {}).get("type") == target:
            return True
        return False

    def __validate_value(self):
        ...

    def insert_in_auxiliary_table(self, table_name, params: tuple):
        if self.__validate_table(table_name=table_name, target="auxiliary_table"):
            if table_name != "company":
                query = f"""
                INSERT INTO {table_name} (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING;
                """
            else:
                query = f"""
                INSERT INTO company (short_name, long_name, display_name, symbol)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (symbol) DO NOTHING;
                """
            self.execute_query(query=query, params=params)

    def insert_market_value(self, market_data: dict, auxiliary_ids: dict):

        query = f"""
            INSERT INTO market_value (company_id, region_id, market_state_id, exchange_id,
            market_id, currency_id, price_hint, financial_currency_id, market_cap, book_value)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

        params = (
            auxiliary_ids["company_id"],
            auxiliary_ids["region_id"],
            auxiliary_ids["market_state_id"],
            auxiliary_ids["exchange_id"],
            auxiliary_ids["market_id"],
            auxiliary_ids["currency_id"],
            market_data["price_hint"],
            auxiliary_ids["currency_id"],
            market_data["market_cap"],
            market_data["book_value"]
        )

        self.execute_query(query=query, params=params)

    def __handle_aux_table(self,
                           table_name: str,
                           comparator: str,
                           comparator_value: str,
                           params: tuple) -> str:

        query = f"""
        SELECT id 
        FROM {table_name}
        WHERE {comparator} = '{comparator_value}'
        """
        if _id := self.select(query, "fetchone"):
            return _id[0]

        else:  # TODO: Here we must insert the values
            self.insert_in_auxiliary_table(table_name=table_name, params=params)
            return self.__handle_aux_table(table_name=table_name,
                                           comparator=comparator,
                                           comparator_value=comparator_value,
                                           params=params)

    @staticmethod
    def __split_data(data: dict) -> tuple[dict, dict]:

        # TODO: Move this to resources
        auxiliary_tables_mapping = {
            "company_id": {
                "table_name": "company",
                "comparator": "symbol",
                "comparator_value": data["symbol"],
                "params": (data["short_name"], data["long_name"], data["display_name"], data["symbol"])
            },
            "region_id": {
                "table_name": "region",
                "comparator": "name",
                "comparator_value": data["region"],
                "params": (data["region"],)
            },
            "market_state_id": {
                "table_name": "market_state",
                "comparator": "name",
                "comparator_value": data["market_state"],
                "params": (data["market_state"],)
            },
            "exchange_id": {
                "table_name": "exchange",
                "comparator": "name",
                "comparator_value": data["exchange"],
                "params": (data["exchange"],)
            },
            "market_id": {
                "table_name": "market",
                "comparator": "name",
                "comparator_value": data["market"],
                "params": (data["market"],)
            },
            "currency_id": {
                "table_name": "currency",
                "comparator": "name",
                "comparator_value": data["currency"],
                "params": (data["currency"],)
            },

        }

        market_value_mapping = {
            "price_hint": data["price_hint"],
            "market_cap": data["market_cap"],
            "book_value": data["book_value"]
        }

        return auxiliary_tables_mapping, market_value_mapping

    def insert_data(self, data: dict):

        (auxiliary_mapping,
         market_value_mapping) = self.__split_data(data=data)

        auxiliary_ids = {
            id_name: self.__handle_aux_table(**values) for id_name, values in auxiliary_mapping.items()
        }

        self.insert_market_value(market_data=market_value_mapping, auxiliary_ids=auxiliary_ids)

    def process_message(self, msg: dict):
        for key, value in msg.items():
            if (data := value.get("data", {})) and (value.get("action") == "insert"):
                self.insert_data(data=data)


