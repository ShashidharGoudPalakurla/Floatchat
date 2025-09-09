# FloatChat - AI-Powered Conversational Interface for ARGO Ocean Data

**FloatChat** is a platform that allows users to explore ARGO oceanographic data using **natural language queries**. It processes complex NetCDF datasets, stores them in relational and vector databases, and provides an interactive frontend for visualization and analysis.

---

## 🚀 Features

- **Data Ingestion:**  
  Converts ARGO NetCDF files into structured data for PostgreSQL and semantic embeddings for Qdrant.  

- **Backend API:**  
  Handles user queries, fetches relevant data from databases, and supports natural language querying.  

- **Frontend Interface:**  
  React-based dashboard for visualizations like depth-time plots, geospatial maps, and tabular summaries.  

- **Optional Dataset Fetcher:**  
  Go service to download NetCDF files automatically from FTP/HTTP sources.


# 🏗 Repo Structure
``````

floatchat/
│
├── data/                   # Raw NetCDF files
├── ingestion/              # Python: NetCDF → PostgreSQL + Qdrant
├── api/                    # FastAPI backend
├── go-fetcher/             # Optional Go: fetch datasets
├── frontend/               # React frontend
├── infra/                  # DB / VectorDB setup scripts
├── .gitignore
└── README.md

``````

# ⚙️ Setup & Installation

## 1. Clone the repo

git clone https://github.com/SyedOwais312/floatchat.git
cd floatchat

## 2. Setup Databases

PostgreSQL: run infra/postgres_init.sql

Qdrant: run infra/qdrant_setup.py (optional)

## 3. Python Services

### Ingestion
cd ingestion
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python main.py

### API
cd api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000

## 4. Frontend
cd frontend
npm install
npm start

## 5. Optional Go Fetcher
cd go-fetcher
go run main.go

#💡 Usage

Visit the frontend: http://localhost:3000

API available at: http://localhost:8000/docs

### Ask queries like:

“Show salinity profiles near the equator in March 2023”

“Compare temperature in Arabian Sea last 6 months”
