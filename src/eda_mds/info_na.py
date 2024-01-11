def info_na(df): 
    """
    This function replicates and extends behaviour of pandas.DataFrame.info() to include row-wise information. 

    This function prints the following information about a DataFrame: 
    - Columns: 
        - Index
        - Name
        - Non-Null Count
        - Dtype
    - Rows: 
        - Count of rows with any Null Values
        - Count of rows with all Null values
        - Descriptive statistics of proportion of Null Values per row.

    Parameters
    ----------
    df : pandas.DataFrame
        _description_
    """