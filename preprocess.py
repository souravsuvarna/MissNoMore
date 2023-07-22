import pandas as pd

def tocsv(file):
    df = pd.read_csv(file)
    return df

def null_columns(df):
    return df.columns[df.isna().any()].tolist()