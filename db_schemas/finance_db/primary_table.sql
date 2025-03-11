CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DROP TABLE IF EXISTS market_value CASCADE;

CREATE TABLE market_value (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),  -- Unique ID for the record
    company_id UUID NOT NULL,
    region_id UUID NOT NULL,
    market_state_id UUID NOT NULL,
    exchange_id UUID NOT NULL,
    market_id UUID NOT NULL,
    currency_id UUID NOT NULL,
    price_hint NUMERIC(10, 2) NOT NULL CHECK (price_hint >= 0),  -- Enforce non-negative values
    financial_currency_id UUID NOT NULL,
    market_cap NUMERIC(18, 2) CHECK (market_cap >= 0),  -- Market cap should not be negative
    book_value NUMERIC(18, 2) CHECK (book_value >= 0),  -- Book value should not be negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Track record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Track updates

    -- Foreign Key Constraints for Data Integrity
    CONSTRAINT fk_company FOREIGN KEY (company_id) REFERENCES company(id) ON DELETE CASCADE,
    CONSTRAINT fk_region FOREIGN KEY (region_id) REFERENCES region(id) ON DELETE CASCADE,
    CONSTRAINT fk_market_state FOREIGN KEY (market_state_id) REFERENCES market_state(id) ON DELETE CASCADE,
    CONSTRAINT fk_exchange FOREIGN KEY (exchange_id) REFERENCES exchange(id) ON DELETE CASCADE,
    CONSTRAINT fk_market FOREIGN KEY (market_id) REFERENCES market(id) ON DELETE CASCADE,
    CONSTRAINT fk_currency FOREIGN KEY (currency_id) REFERENCES currency(id) ON DELETE CASCADE,
    CONSTRAINT fk_financial_currency FOREIGN KEY (financial_currency_id) REFERENCES currency(id) ON DELETE CASCADE
);

-- Add trigger to update `updated_at` on row update
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON market_value
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();
