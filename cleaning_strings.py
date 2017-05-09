import pandas as pd

def get_dtypes(df, cols_list, dtype1 = float, dtype2 = str):
    '''
    Get dtypes for importing a dataframe.

    Input:
    df: dataframe to get columns from
    cols_list: list of columns of a specific dtype
    dtype1: dtype of columns in cols_list, default = float
    dtype2: dtype of other columns, default = str

    Output:
    dtypes: dictionary of {column_names:dtype}
    '''

    col_dtype1 = df[cols_list].columns
    col_dtype2 = df.drop(col_dtype1, axis = 1)

    dict1 = {key: dtype1 for key in col_dtype1}
    dict2 = {key: dtype2 for key in col_dtype2}

    return {**dict1, **dict2}

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