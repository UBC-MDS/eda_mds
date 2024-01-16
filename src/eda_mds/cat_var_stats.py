def cat_var_stats(df):
    """
    This function creates summary statistics about categorical variables in the dataframe. Number of unique values,
    frequency of values and whether some categories should binned will be among the info that will be presented.

    This function prints the following information about a DataFrame:
    - Number of unique values per categorical column.
    - Frequency of values for categorical columns.
    - Binning recommendations for low frequency values for categorical columns.


    Parameters
    ----------
    df : pandas.DataFrame
        A pandas dataframe.

    Returns
    -------
    None :
        This function prints the following information and returns None.

    """
# notes: take in outliers of the count

# Defensive
# 1. No categorical column
# 2. All unique values 
# 3. Correctly rejects column
# 4. Output is correct