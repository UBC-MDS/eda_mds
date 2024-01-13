def info_na(df):
    """
    This function replicates and extends behaviour of pandas.DataFrame.info().
    New information will consist of row-level summary statistics for null values to characterize dataframe structure.

    This function prints the following information about a DataFrame:
    - DataFrame Class
    - Shape:
    - Columns:
        - Index
        - Name
        - Non-Null Count
        - Dtype
    - Rows:
        - Count of rows with any Null Values.
        - Count of rows with all Null values.
        - Descriptive statistics of proportion of Null Values per row.
    - Memory Usage

    Parameters
    ----------
    df : pandas.DataFrame
        A tidy dataframe.

    """
