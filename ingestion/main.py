import os
import xarray as xr
import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch

# CONFIG
DATA_DIR ="./data"  # folder with NetCDF files
BULK_SIZE = 1000      # rows per batch insert
DB_CONFIG = {
    "host": "localhost",
    "database": "floatchatai",
    "user": "postgres",
    "password": "Owais@786"
}

def load_netcdf_to_df(file_path):
    ds = xr.open_dataset(file_path)
    rows = []

    for prof in range(ds.sizes["N_PROF"]):
        for level in range(ds.sizes["N_LEVELS"]):
            row = {
                "N_PROF": int(prof),
                "N_LEVELS": int(level),
                "JULD": pd.to_datetime(ds['JULD'][prof].values).to_pydatetime(),
                "LATITUDE": float(ds['LATITUDE'][prof].values),
                "LONGITUDE": float(ds['LONGITUDE'][prof].values),
                "PRES": float(ds['PRES'][prof, level].values),
                "TEMP": float(ds['TEMP'][prof, level].values),
                "PSAL": float(ds['PSAL'][prof, level].values)
            }
            rows.append(row)
            print("Data inserted -> 1 row")
    
    df = pd.DataFrame(rows)
    return df

def insert_to_postgres(df, conn):
    sql = """
        INSERT INTO profiles (N_PROF, N_LEVELS, JULD, LATITUDE, LONGITUDE, PRES, TEMP, PSAL)
        VALUES (%(N_PROF)s, %(N_LEVELS)s, %(JULD)s, %(LATITUDE)s, %(LONGITUDE)s, %(PRES)s, %(TEMP)s, %(PSAL)s)
    """
    with conn.cursor() as cur:
        execute_batch(cur, sql, df.to_dict('records'), page_size=BULK_SIZE)
    conn.commit()
    print("Data inserted successfully!")

def process_all():
    conn = psycopg2.connect(**DB_CONFIG)
    
    for file in os.listdir(DATA_DIR):
        if file.endswith(".nc"):
            file_path = os.path.join(DATA_DIR, file)
            print(f"Processing {file_path}...")
            df = load_netcdf_to_df(file_path)
            print(f"Data shape: {df.shape}")
            insert_to_postgres(df, conn)
    
    conn.close()

if __name__ == "__main__":
    process_all()
