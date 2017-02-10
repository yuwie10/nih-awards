import pandas as pd

def strip_df(df, *args):
    '''
    
    Strips final character from each column in a df.
    
    '''
    for arg in args:
        df = df.apply(lambda s: s.str.strip(arg))
    return df

def split_rows(df, col_name, by):
    '''
    
    Split rows of a df by a particular delimiter
    
    '''
    df_copy = df.copy()
    s = df_copy[col_name].str.split(by).apply(pd.Series, 1).stack()
    s.index = s.index.droplevel(-1)
    s.name = col_name
    del df_copy[col_name]
    return df_copy.join(s)

def strip_series(df, col_list, strip = '(contact)'):
    '''
    
    Strips string from a series (column in df)
    
    '''
    for col in col_list:
        df[col] = df[col].str.strip(strip)
    return df