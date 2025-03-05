DB_NAME=mydatabase
DB_USER=myuser
DB_HOST=localhost
DB_PORT=5432
DB_PASSWORD=mypassword

AUXILIAR_TABLES_SCHEMA=db_schemas/finance_db/auxiliary_tables.sql
PRIMARY_TABLE_SCHEMA=db_schemas/finance_db/primary_table.sql

define psql_exec
PGPASSWORD=$(DB_PASSWORD) psql -U $(DB_USER) -h $(DB_HOST) -p $(DB_PORT) -d postgres -c "$(1)"
endef

.PHONY: db-create db-schema db-reset

## Create database
db-create:
	@echo "Creating database $(DB_NAME)..."
	$(call psql_exec, "CREATE DATABASE $(DB_NAME);")
	@echo "Database $(DB_NAME) created."

## Create tables from schema.sql
db-schema:
	@echo "Applying schema..."
	PGPASSWORD=$(DB_PASSWORD) psql -U $(DB_USER) -h $(DB_HOST) -p $(DB_PORT) -d $(DB_NAME) -f $(AUXILIAR_TABLES_SCHEMA)
	@echo "Auxliary tables created successfully."
	PGPASSWORD=$(DB_PASSWORD) psql -U $(DB_USER) -h $(DB_HOST) -p $(DB_PORT) -d $(DB_NAME) -f $(PRIMARY_TABLE_SCHEMA)
	@echo "Primary table created successfully."

## Drop and recreate database
db-reset:
	@echo "Resetting database..."
	$(call psql_exec, "DROP DATABASE IF EXISTS $(DB_NAME);")
	$(MAKE) db-create
	$(MAKE) db-schema
