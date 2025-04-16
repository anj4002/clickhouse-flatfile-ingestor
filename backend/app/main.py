from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.ingest import router as ingest_router
import logging

# Configure logging in main.py as well
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest_router)

@app.on_event("startup")
async def startup_event():
    logging.info("FastAPI application started") # Log at startup

@app.on_event("shutdown")
async def shutdown_event():
    logging.info("FastAPI application stopped") # Log at shutdown
