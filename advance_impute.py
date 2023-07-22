import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression


def knn(data,order):
    numerical_cols = data.select_dtypes(include=[np.number]).columns

    # Create a copy of the DataFrame with only the target column and numerical columns
    X = data[numerical_cols].copy()

    # Instantiate the KNNImputer with the desired number of neighbors
    imputer = KNNImputer(n_neighbors=order)

    # Fit and transform the imputer on the target column
    X_imputed = imputer.fit_transform(X).round(2)

    # Combine the imputed column with the rest of the DataFrame
    data[numerical_cols] = X_imputed
    
    return data


def iterative(data):
    # Filter numerical columns for imputation
    numerical_cols = data.select_dtypes(include=[np.number]).columns

    # Create a copy of the DataFrame with only the target column and numerical columns
    X = data[numerical_cols].copy()

    # Instantiate the IterativeImputer
    imputer = IterativeImputer()

    # Fit and transform the imputer on the target column
    X_imputed = imputer.fit_transform(X).round(2)

    # Combine the imputed column with the rest of the DataFrame
    data[numerical_cols] = X_imputed
    
    return data