import pandas as pd 
import numpy as np

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

def sr_transformation(df, card_var, response_col):
    '''
    Transform high cardinal data to a continuous variable to use in predictive model:
    
    supervised ratio of level = #times level is in response group / total in response group
    
    Inputs: 
    Output: 
    '''

    #creates a dataframe where counts of response is grouped by the cardinal variable
    #fills missing values with 0
    counts = pd.DataFrame(df.groupby([card_var, response_col]).size(), columns = ['counts'])
    counts = counts.unstack('funding_group').fillna(0).stack()

    #list of distinct values of cardinal variable
    #excluding nulls
    unique_card = df[card_var].dropna().unique().tolist()

    #total counts within each value of the cardinal variable
    value_counts = df[card_var].value_counts()

    #list of response category values
    response_groups = df[response_col].unique().tolist()
    
    df_ratios = pd.DataFrame(columns = ['low', 'med-low', 'med-high', 'high']) #response_groups
    for card in unique_card:
    	ratios = {}
    	for response in response_groups:
    		ratios[response] = (counts.loc[card, response] / value_counts[card]).item()
    	df_ratios.loc[card] = ratios

    return df_ratios





