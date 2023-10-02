import numpy as np

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
            
    