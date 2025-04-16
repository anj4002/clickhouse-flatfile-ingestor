from pydantic import BaseModel, Field
from typing import List, Optional

class ClickHouseConfig(BaseModel):
    host: str = Field(..., description="ClickHouse host address")
    port: int = Field(..., description="ClickHouse port number")
    database: str = Field(..., description="ClickHouse database name")
    user: str = Field(..., description="ClickHouse username")
    jwt_token: str = Field(..., description="ClickHouse JWT token")

class FlatFileConfig(BaseModel):
    filepath: str = Field(..., description="Path to the flat file")
    delimiter: str = Field(..., description="Delimiter used in the flat file")

class IngestionRequest(BaseModel):
    source: str = Field(..., description="Source of the data (e.g., 'ClickHouse', 'FlatFile')")
    target: str = Field(..., description="Target for the data (e.g., 'ClickHouse', 'FlatFile')")
    clickhouse_config: Optional[ClickHouseConfig] = Field(None, description="ClickHouse configuration (required if source or target is ClickHouse)")
    flatfile_config: Optional[FlatFileConfig] = Field(None, description="Flat file configuration (required if source or target is FlatFile)")
    selected_columns: List[str] = Field(..., description="List of columns to select")
    table: Optional[str] = Field(None, description="Table name (required for ClickHouse)")

class IngestionResponse(BaseModel):
    status: str = Field(..., description="Status of the ingestion process ('success' or 'error')")
    records: int = Field(..., description="Number of records processed")
