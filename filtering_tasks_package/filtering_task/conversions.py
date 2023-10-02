import numpy as np


def convert_and_multiply(value):
    if not isinstance(value, str):
        return 0
    if value.endswith('G'):
        num_value=float(value[:-2])*1000
    if value.endswith('M'):
        num_value=float(value[:-2])*1
    if value.endswith('T'):
        num_value=float(value[:-2])*1000000
    else:
        return value
    return int(num_value)        


def columns_to_2dp(df, columns):
    df[columns]= df[columns].fillna(0)
    
    # Custom rounding function
    def round_up(x):
        if x % 1 >= 0.005:
            return np.ceil(x*100)/100
        else:
            return np.floor(x)
        
    df[columns] = df[columns].applymap(round_up)
    return df
            
    