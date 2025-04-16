**🚀 Bidirectional ClickHouse & Flat File Data Ingestion Tool**

This project is a full-stack web-based application that enables bidirectional data ingestion between a ClickHouse database and flat files (CSV). The tool supports authentication, selective column-level data transfers, preview, and ingestion metrics reporting. It provides a clean UI to help users connect, configure, preview, and transfer data without manual scripting.

📦 Features
🔁 Bidirectional ingestion:

ClickHouse ➝ Flat File

Flat File ➝ ClickHouse

🛡️ JWT-based authentication for ClickHouse

📑 Schema detection for both ClickHouse and CSVs

✅ Selective column-level transfer

📊 Ingestion result with record count and optional preview

⚙️ Setup & Configuration
🧰 Prerequisites
Ensure the following are installed:

Python 3.8+

Node.js & npm

Docker Desktop

Git (optional)

🗂️ Directory Structure
bash
Copy code
clickhouse-flatfile-ingestor/
├── backend/         # FastAPI backend for ingestion logic
├── frontend/        # React frontend for UI
└── clickhouse/      # Docker ClickHouse setup
⚙️ ClickHouse Setup via Docker
Open terminal and navigate to the project folder:

bash
Copy code
cd clickhouse-flatfile-ingestor/clickhouse
Run ClickHouse:

bash
Copy code
docker-compose up -d
This exposes ClickHouse at:

Port 8123 (HTTP interface)

Username: default

Password: clickpass123

🐍 Backend Setup (FastAPI)
Navigate to the backend folder:

bash
Copy code
cd ../backend
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Mac/Linux
Install backend dependencies:

bash
Copy code
pip install -r requirements.txt
Start the backend server:

bash
Copy code
uvicorn app.main:app --reload
Server will run on:
http://127.0.0.1:8000

🌐 Frontend Setup (React)
Navigate to frontend folder:

bash
Copy code
cd ../frontend
Install dependencies:

bash
Copy code
npm install
Start the development server:

bash
Copy code
npm run dev
Frontend will be available at:
http://localhost:5173

🧪 How to Use
Select Source and Target (ClickHouse or Flat File).

Enter relevant connection details.

Click Load Columns or Get Tables depending on source.

Choose desired columns.

Click Start Ingestion.

View success message with record count (and preview, if enabled).

📈 API Endpoints

Method	Endpoint	Purpose
POST	/ingest	Run ingestion between sources
POST	/clickhouse/tables	Fetch list of ClickHouse tables
POST	/flatfile/schema	Get CSV column schema
📌 Example CSV Path
When ingesting from/to flat files, use:

bash
Copy code
C:/clickhouse-flatfile-ingestor/sample_input.csv
Ensure the file exists at the specified path.
