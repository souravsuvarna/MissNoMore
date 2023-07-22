import pandas as pd
import numpy as np

def replace_with_zero(data,val):
    data[val] = data[val].fillna(0)
    return data

def mean(data,val):
    data[val] = data[val].fillna(data[val].mean()).round(2)
    return data

def median(data,val):
    data[val] = data[val].fillna(data[val].median())
    return data