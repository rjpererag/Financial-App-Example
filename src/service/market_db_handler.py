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

    def insert_in_market_value(self, data: dict):
        # TODO: Here we must iterate over the aux tables to collect the IDs
        # mapping = {name: {table_name: str, id: UUID}}

        # Step 1: Get IDs from auxiliary tables (company_id, region_id, market_state_id, exchange_id,
        # market_id, currency_id, financial_currency_id)

        params = (data["short_name"], data["long_name"], data["display_name"], data["symbol"])

        response = self.__handle_aux_table(table_name="company",
                                           comparator="symbol",
                                           comparator_value=data["symbol"],
                                           params=params)

        print(response)


    def process_message(self):
        ...
