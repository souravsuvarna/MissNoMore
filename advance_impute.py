import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

#1. KNN
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

#2. Iterative
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

#3.SimpleImputer (Mean)
def simple_mean(data):
    # Filter numerical columns for imputation
    numerical_cols = data.select_dtypes(include=[np.number]).columns

    # Create a copy of the DataFrame with only the target column and numerical columns
    X = data[numerical_cols].copy()

    # Instantiate the SimpleImputer with the desired strategy ('mean', 'median', 'most_frequent', or 'constant')
    imputer = SimpleImputer(strategy='mean')

    # Fit and transform the imputer on the target column
    X_imputed = imputer.fit_transform(X).round(2)

    # Combine the imputed column with the rest of the DataFrame
    data[numerical_cols] = X_imputed 
    
    return data   

#4.SimpleImputer (Median)
def simple_median(data):
    # Filter numerical columns for imputation
    numerical_cols = data.select_dtypes(include=[np.number]).columns

    # Create a copy of the DataFrame with only the target column and numerical columns
    X = data[numerical_cols].copy()

    # Instantiate the SimpleImputer with the desired strategy ('mean', 'median', 'most_frequent', or 'constant')
    imputer = SimpleImputer(strategy='median')

    # Fit and transform the imputer on the target column
    X_imputed = imputer.fit_transform(X).round(2)

    # Combine the imputed column with the rest of the DataFrame
    data[numerical_cols] = X_imputed
    
    return data

#5.Random Forest
def random_forest(data):
    # Filter numerical columns for imputation
    numerical_cols = data.select_dtypes(include=[np.number]).columns

    # Create a copy of the DataFrame with only the target column and numerical columns
    X = data[numerical_cols].copy()

    # Instantiate the IterativeImputer with RandomForestRegressor as the estimator
    imputer = IterativeImputer(estimator=RandomForestRegressor())

    # Fit and transform the imputer on the target column
    X_imputed = imputer.fit_transform(X).round(2)

    # Combine the imputed column with the rest of the DataFrame
    data[numerical_cols] = X_imputed
    
    return data

#6. Decision Tree
def decision_tree(data):
    # Filter numerical columns for imputation
    numerical_cols = data.select_dtypes(include=[np.number]).columns

    # Create a copy of the DataFrame with only the target column and numerical columns
    X = data[numerical_cols].copy()

    # Instantiate the IterativeImputer with DecisionTreeRegressor as the estimator
    imputer = IterativeImputer(estimator=DecisionTreeRegressor())

    # Fit and transform the imputer on the target column
    X_imputed = imputer.fit_transform(X).round(2)

    # Combine the imputed column with the rest of the DataFrame
    data[numerical_cols] = X_imputed
    
    return data

#7. Linear Regresion
def linear_reg(data):
    # Filter numerical columns for imputation
    numerical_cols = data.select_dtypes(include=[np.number]).columns

    # Create a copy of the DataFrame with only the target column and numerical columns
    X = data[numerical_cols].copy()

    # Instantiate the IterativeImputer with LinearRegression as the estimator
    imputer = IterativeImputer(estimator=LinearRegression())

    # Fit and transform the imputer on the target column
    X_imputed = imputer.fit_transform(X).round(2)

    # Combine the imputed column with the rest of the DataFrame
    data[numerical_cols] = X_imputed
    
    return data

#8. Random Sampling
def random_sampling(data):
    # Filter numerical columns for imputation
    numerical_cols = data.select_dtypes(include=[np.number]).columns

    # Create a copy of the DataFrame with only the target column and numerical columns
    X = data[numerical_cols].copy()

    # Perform Random Sample Imputation
    for col in numerical_cols:
        missing_mask = X[col].isnull()
        non_missing_values = X.loc[~missing_mask, col]
        X.loc[missing_mask, col] = np.random.choice(non_missing_values, size=missing_mask.sum())

    # Combine the imputed column with the rest of the DataFrame
    data[numerical_cols] = X
    
    return data
    