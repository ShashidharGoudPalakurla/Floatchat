import xarray as xr
import pandas as pd
import glob

def load_argo_netcdf(folder_path):
    """Load all NetCDF files from folder and return as a single DataFrame"""
    files = glob.glob(f"{folder_path}/*.nc")
    dfs = []
    for file in files:
        ds = xr.open_dataset(file)
        df = pd.DataFrame({
            'float_id': ds['PLATFORM_NUMBER'].values[0],
            'time': pd.to_datetime(ds['JULD'].values, unit='D', origin=pd.Timestamp('1950-01-01')),
            'latitude': ds['LATITUDE'].values,
            'longitude': ds['LONGITUDE'].values,
            'depth': ds['PRES'].values,
            'temperature': ds['TEMP'].values,
            'salinity': ds['PSAL'].values
        })
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)
