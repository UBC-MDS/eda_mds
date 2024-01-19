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
    - Memory Usage
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
            "column": df.columns.values,
            "null count": df.isna().sum(axis=0),
            "null %": (df.isna().sum(axis=0) / df.shape[0] * 100).round(2),
            "dtype": df.dtypes,
        }
    )

    row_info = pd.Series(
        {
            "total rows": df.shape[0],
            "any null count": df.isna().any(axis=1).sum(),
            "any null %": (df.isna().any(axis=1).sum() / df.shape[0] * 100).round(2),
            "all null count": df.isna().all(axis=1).sum(),
            "all null %": (df.isna().all(axis=1).sum() / df.shape[0] * 100).round(2),
            "mean null count": df.isna().sum(axis=1).mean().round(2),
            "std.dev null count": df.isna().sum(axis=1).std().round(2),
            "max null count": df.isna().sum(axis=1).max(),
            "min null count": df.isna().sum(axis=1).min()
        }
    )

    suffix = ["B", "KB", "MB", "GB", "TB"]
    memory_bytes = df.memory_usage(deep=True).sum()  
    n = 0
    while memory_bytes > 2 ** 10: 
        memory_bytes = memory_bytes / 2 ** 10 
        n += 1
    memory_info = f"{np.round(memory_bytes, 1)} {suffix[n]}"

    # print(type_info)
    # print(shape_info)
    # print(column_info)
    # print(row_info)
    # print(memory_info)


    output = f"""
type: {type_info}
shape: {shape_info}
memory usage: {memory_info}
--------
columns:
{column_info.to_string(index=False)}
-----
rows:
{row_info.to_string()}
"""
    
    print(output)

# Tasks: 
# - Dataframe class
# - Dataframe shape
# - Dataframe memory usage 
# - Formatting for printing