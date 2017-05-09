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

def view_col_info(csv, cols_list = None, col_name = 'column_name'):
	'''
	View description(s) of columns 

	Inputs: path/name of csv file, list of columns to view and
	name of column to filter on
	Output: df with column descriptions
	'''

	df = pd.read_csv(csv)
	pd.set_option('display.max_colwidth', 5000)

	if cols_list == None:
		return df
	else:
		descriptions = []
		for col in cols_list:
			descriptions.append(df.ix[df[col_name] == col])
		return pd.concat(descriptions)





