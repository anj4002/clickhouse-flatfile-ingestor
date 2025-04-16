import pandas as pd
from clickhouse_connect import get_client
import logging

def fetch_clickhouse_data(config, table, columns):
    """
    Fetches data from ClickHouse and returns it as a Pandas DataFrame.
    """
    try:
        client = get_client(
            host=config.host,
            port=int(config.port),
            username=config.user,
            password=config.jwt_token,
            database=config.database
        )
        query = f"SELECT {','.join(columns)} FROM {table}"
        logging.info(f"Executing ClickHouse query: {query}")  # Log the query
        result = client.query(query)
        df = pd.DataFrame(result.result_set, columns=result.column_names)
        logging.info(f"Fetched {len(df)} rows from ClickHouse")
        return df
    except Exception as e:
        logging.error(f"Error fetching data from ClickHouse: {e}")
        raise  # Re-raise the exception to be caught in ingest.py

def write_flat_file(df, config):
    """
    Writes a Pandas DataFrame to a flat file (e.g., CSV).
    """
    try:
        logging.info(f"Writing data to flat file: {config.filepath}, delimiter: {config.delimiter}")
        df.to_csv(config.filepath, index=False, sep=config.delimiter)
        count = int(df.shape[0])
        logging.info(f"Wrote {count} rows to flat file: {config.filepath}")
        return count
    except Exception as e:
        logging.error(f"Error writing to flat file: {e}")
        raise  # Re-raise

def read_flat_file(config):
    """
    Reads a flat file (e.g., CSV) into a Pandas DataFrame.
    """
    try:
        logging.info(f"Reading data from flat file: {config.filepath}, delimiter: {config.delimiter}")
        df = pd.read_csv(config.filepath, delimiter=config.delimiter)
        logging.info(f"Read {len(df)} rows from flat file: {config.filepath}")
        return df
    except Exception as e:
        logging.error(f"Error reading flat file: {e}")
        raise  # Re-raise

def write_to_clickhouse(df, config, table_name):
    """
    Writes a Pandas DataFrame to a ClickHouse table.
    """
    try:
        client = get_client(
            host=config.host,
            port=int(config.port),
            username=config.user,
            password=config.jwt_token,
            database=config.database
        )

        #  Check if table exists
        table_exists_query = f"SHOW TABLES LIKE '{table_name}'"
        if client.query(table_exists_query).result_set:
             logging.warning(f"Table {table_name} already exists.  Dropping it.")
             client.command(f"DROP TABLE IF EXISTS {table_name}")

        # Determine ClickHouse data types from Pandas dtypes.  Important!
        clickhouse_types = []
        for col, dtype in df.dtypes.items():
            if pd.api.types.is_numeric_dtype(dtype):
                clickhouse_type = 'Float64'  # Or Integer, decide based on your needs
            elif pd.api.types.is_datetime64_any_dtype(dtype):
                clickhouse_type = 'DateTime'
            else:
                clickhouse_type = 'String'  # Default to String

            clickhouse_types.append(f"{col} {clickhouse_type}")

        create_query = f"""
            CREATE TABLE {table_name} (
                {', '.join(clickhouse_types)}
            ) ENGINE = MergeTree() ORDER BY tuple()
        """
        logging.info(f"Creating ClickHouse table: {create_query}")
        client.command(create_query)

        logging.info(f"Inserting {len(df)} rows into ClickHouse table: {table_name}")
        client.insert_df(table=table_name, df=df)
        count = int(df.shape[0])
        logging.info("Insert completed.")
        return count
    except Exception as e:
        logging.error(f"Error writing to ClickHouse: {e}")
        raise  # Re-raise

