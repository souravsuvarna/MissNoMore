import pandas as pd
import numpy as np

def tocsv(file):
    df = pd.read_csv(file)
    df.replace("-", np.nan, inplace=True)
    return df

def null_columns(df):
    numeric_columns = df.select_dtypes(include='number').columns
    # Select columns with NA values
    na_columns = df[numeric_columns].columns[df[numeric_columns].isna().any()].tolist()
    columns_with_na = na_columns
    
    return columns_with_na