CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE company (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    short_name VARCHAR(255) NOT NULL,
    long_name VARCHAR(255),
    display_name VARCHAR(255),
    symbol VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE region (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE market_state (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE exchange (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE market (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE currency (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE market_value (
    company_id UUID REFERENCES company(id) ON DELETE CASCADE,
    region_id UUID REFERENCES region(id),
    market_state_id UUID REFERENCES market_state(id),
    exchange_id UUID REFERENCES exchange(id),
    market_id UUID REFERENCES market(id),
    currency_id UUID REFERENCES currency(id),
    price_hint FLOAT,
    financial_currency_id UUID REFERENCES currency(id),
    market_cap FLOAT,
    book_value FLOAT
);
