from fastapi import APIRouter, HTTPException
from app.schemas import IngestionRequest, IngestionResponse
from app.utils import fetch_clickhouse_data, write_flat_file, read_flat_file, write_to_clickhouse
import logging

router = APIRouter()
# Configure logging (optional, but highly recommended for debugging)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@router.post("/ingest", response_model=IngestionResponse)
def ingest_data(req: IngestionRequest):
    try:
        logging.info(f"Incoming request: {req.dict()}") # Use logging
        # print("✅ Incoming request:", req.dict())

        if req.source == "ClickHouse" and req.target == "FlatFile":
            df = fetch_clickhouse_data(req.clickhouse_config, req.table, req.selected_columns)
            count = write_flat_file(df, req.flatfile_config)
            # print("✅ Inserted", count, "Type:", type(count))
            logging.info(f"Inserted {count} rows into FlatFile") # Use logging
            return IngestionResponse(status="success", records=int(count))  

        elif req.source == "FlatFile" and req.target == "ClickHouse":
            df = read_flat_file(req.flatfile_config)
            count = write_to_clickhouse(df, req.clickhouse_config, req.table)
            logging.info(f"Inserted {count} rows into ClickHouse") # Use logging
            # print(f"✅ Inserted {count} rows into ClickHouse. Type: {type(count)}")
            return IngestionResponse(status="success", records=int(count))  

        else:
            logging.error(f"Invalid source/target combination: {req.source} -> {req.target}")
            raise HTTPException(status_code=400, detail="Invalid source/target combination")

    except Exception as e:
        # print(f"❌ Backend Error: {str(e)} (type: {type(e)})")
        error_message = f"Backend Error: {str(e)} (type: {type(e)})"
        logging.exception(error_message)  # Log the *entire* exception traceback
        raise HTTPException(status_code=500, detail=error_message)
       # raise HTTPException(status_code=500, detail=str(e))

       
