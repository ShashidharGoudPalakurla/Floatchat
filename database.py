from sqlalchemy import create_engine

def save_to_sql(df, db_path='argo_data.db', table_name='argo_floats'):
    """Save DataFrame to SQLite/PostgreSQL"""
    engine = create_engine(f'sqlite:///{db_path}')
    df.to_sql(table_name, engine, if_exists='replace', index=False)
