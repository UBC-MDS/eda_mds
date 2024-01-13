def describe_outliers(df, threshold_factor=1.5):
    """
    Extends the functionality of pandas.Dataframe.describe() for numeric data by 
    additionally providing a count of lower-tail and upper-tail outliers. 

    If the data contains numerical values, the returned description includes the following
    information:
    
    - count: The number of non-null observations.
    - mean: The mean value.
    - std: The standard deviation.
    - min: the minimum value.
    - 25%: The 25% percentile (Q1).
    - 50%: The 50% percentile (Q2).
    - 75%: The 75% percentile (Q3).
    - max: the maximum value.
    - lower-tail outliers: count of values significantly smaller than the majority of data.
    - upper-tail outliers: count of values significantly larger than the majority of data.

    Outliers are calculated using Interquartile Range (IQR) method for outlier detection.
    Lower-tail outliers are observations less than Q1 - threshold_factor*IQR 
    Upper-tail outliers are observations greater than Q3 + threshold_factor*IQR 

    Parameters
    ----------
    df : pandas.DataFrame
        A tidy dataframe.
    
    threshold : float, optional
        The scalar used in outlier detection. It must be a positive numeric value. A higher value reduces 
        the sensitivity of outlier detection.

    Returns
    -------

    None. Descriptive information is printed. 

    """