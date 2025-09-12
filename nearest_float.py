from geopy.distance import geodesic

def find_nearest(df, lat, lon, top_n=3):
    """Find nearest ARGO floats to given latitude and longitude"""
    df = df.copy()
    df['distance_km'] = df.apply(lambda row: geodesic((lat, lon), (row['latitude'], row['longitude'])).km, axis=1)
    return df.nsmallest(top_n, 'distance_km')
