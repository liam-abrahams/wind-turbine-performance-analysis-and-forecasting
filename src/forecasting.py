import pandas as pd
import numpy as np

def replace_outliers_iqr(df, column):
    '''
    Simple function used to replace outliers from a dataset column using the
    Interquartile Range (IQR) method and a linear interpolation to replace them
    '''
    Q1 = df[column].quantile(0.25) 
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5*IQR    
    upper = Q3 + 1.5*IQR

    df[column] = df[column].mask((df[column] < lower) | (df[column] > upper))
    outliers = df[column].isna().sum()

    df[column] = df[column].interpolate(method="time")

    return df, outliers