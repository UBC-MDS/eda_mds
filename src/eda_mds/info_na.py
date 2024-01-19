import numpy as np
import pandas as pd
import warnings


def info_na(df):
    """
    This function replicates and extends behaviour of pandas.DataFrame.info().
    New information will consist of row-level summary statistics for null values to characterize dataframe structure.

    This function prints the following information about a DataFrame:
    - DataFrame Type
    - Shape:
    - Columns:
        - Index
        - Name
        - Null Count
        - Null Percentage
        - Dtype
    - Rows:
        - Total Rows: 
        - Any Null Count: Count of rows with any Null Values.
        - Any Null Percent: Percentage of rows with any Null Values. 
        - All Null Count: Count of rows with all Null Values.
        - All Null Percent: Percentage of rows with all Null Values. 
        - Mean Null Count: Average number of Null Values per row.
        - Std.Dev Null Count: Standard devation of the number of Null Values per row. 
        - Max Null Count: The maximum number of Null Values found in a row.
        - Min Null Count: The minimum number of Null Values found in a row. 
    - Memory Usage

    Parameters
    ----------
    df : pandas.DataFrame
        A tidy dataframe.

    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input `df` must be a Pandas DataFrame")

    if pd.isna(df).all(axis=None):
        warnings.warn("Input `df` contains all NA values")

    type_info = type(df)

    shape_info = df.shape

    column_info = pd.DataFrame(
        {
            "#": np.arange(df.shape[1]),
            "Column": df.columns.values,
            "Null Count": df.isna().sum(axis=0),
            "Null %": (df.isna().sum(axis=0) / df.shape[0] * 100).round(2),
            "dtype": df.dtypes,
        }
    )

    row_info = pd.Series(
        {
            "Total Rows": df.shape[0],
            "Any Null Count": df.isna().any(axis=1).sum(),
            "Any Null %": (df.isna().any(axis=1).sum() / df.shape[0] * 100).round(2),
            "All Null Count": df.isna().all(axis=1).sum(),
            "All Null %": (df.isna().all(axis=1).sum() / df.shape[0] * 100).round(2),
            "Mean Null Count": df.isna().sum(axis=1).mean().round(2),
            "Std.Dev Null Count": df.isna().sum(axis=1).std().round(2),
            "Max Null Count": df.isna().sum(axis=1).max(),
            "Min Null Count": df.isna().sum(axis=1).min()
        }
    )

    suffix = ["B", "KB", "MB", "GB", "TB"]
    memory_bytes = df.memory_usage(deep=True).sum()  
    n = 0
    while memory_bytes > 2 ** 10: 
        memory_bytes = memory_bytes / 2 ** 10 
        n += 1
    memory_info = f"{np.round(memory_bytes, 1)} {suffix[n]}"

    print(type_info)
    print(shape_info)
    print(column_info)
    print(row_info)
    print(memory_info)

# Tasks: 
# - Dataframe class
# - Dataframe shape
# - Dataframe memory usage 
# - Formatting for printing