import pandas as pd
import numpy as np

#1. Replace Zero
def replace_with_zero(data,val):
    data[val] = data[val].fillna(0)
    return data

#2. Mean
def mean(data,val):
    data[val] = data[val].fillna(data[val].mean()).round(2)
    return data

#3. Median
def median(data,val):
    data[val] = data[val].fillna(data[val].median())
    return data

#4. Mode
def mode(data,val):
    data[val] = data[val].fillna(data[val].mode()[0])
    return data

#5. Forward Fill
def forward_fill(data,val):
    data[val] = data[val].fillna(method='ffill')
    return data

#6. Backward Fill
def backward_fill(data,val):
    data[val] = data[val].fillna(method='bfill')
    return data

#7. Linear
def interpolate_linear(data,val):
    data[val] = data[val].interpolate(method='slinear').round(2)
    return data

#8. Quadratic
def interpolate_quadratic(data,val):
    data[val] = data[val].interpolate(method='quadratic').round(2)
    return data    

#9.Cubic
def interpolate_cubic(data,val):
    data[val] = data[val].interpolate(method='cubic').round(2)
    return data 