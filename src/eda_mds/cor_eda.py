"""
    Perform exploratory data analysis (EDA) by calculating the correlation between numerical variables.
    This function isolates the numerically variables from the given dataset and handles NA values, 
    calculates the correlation between each pair of variables, and displays the results in a table format.

    Parameters:
    dataset (DataFrame): The DataFrame should include various types of variables
    na_handling (str, optional): Specifies the method to handle missing values (NAs). Options are 'drop', 'mean', 'median', and 'value'. Default is 'drop'.
        - 'drop': Drops rows with any NAs.
        - 'mean': Replaces NAs with the mean value of the column.
        - 'median': Replaces NAs with the median value of the column.
        - 'value': Replaces NAs with a selected value.

    Returns:
    DataFrame: A DataFrame containing the correlation values between each pair of numerical variables.

    Example:
    cor_eda(data, na_handling='mean')
               age    salary
    age     1.0000   0.9769
    salary  0.9769   1.0000

"""