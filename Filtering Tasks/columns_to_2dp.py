import numpy as np

def columns_to_2dp(df, columns):
    df[columns]= df[columns].fillna(0)
    
    def round_up(x):
        if x % 1 >= 0.005:
            return np.
            
    