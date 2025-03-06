# TODO: Later work on making this dynamically using the db connection

__tables_types = {
    "aux": "auxiliary_table",
    "primary": "primary"
}

__aux_tables_attributes = {
    "id": {"type": "UUID"},
    "name": {"type": "varchar"},
}

__company_table_attributes = {
    "id": {"type": "UUID"},
    "short_name": {"type": "varchar"},
    "long_name": {"type": "varchar"},
    "display_name": {"type": "varchar"},
    "symbol": {"type": "varchar"},
}

__market_value_table_attributes = {
    "id":  {"type": "UUID"},
    "company_id":  {"type": "UUID"},
    "region_id":  {"type": "UUID"},
    "market_state_id":  {"type": "UUID"},
    "exchange_id":  {"type": "UUID"},
    "market_id":  {"type": "UUID"},
    "currency_id":  {"type": "UUID"},
    "price_hint":  {"type": "NUMERIC"},
    "financial_currency_id":  {"type": "UUID"},
    "market_cap":  {"type": "NUMERIC"},
    "book_value":  {"type": "NUMERIC"},
}


db_schema = {
    "market_state": {"type": __tables_types["aux"], "attributes": __aux_tables_attributes},
    "exchange": {"type": __tables_types["aux"], "attributes": __aux_tables_attributes},
    "market": {"type": __tables_types["aux"], "attributes": __aux_tables_attributes},
    "currency": {"type": __tables_types["aux"], "attributes": __aux_tables_attributes},
    "region": {"type": __tables_types["aux"], "attributes": __aux_tables_attributes},
    "company": {"type": __tables_types["aux"], "attributes": __company_table_attributes},
    "market_value": {"type": __tables_types["primary"], "attributes": __market_value_table_attributes},
}
