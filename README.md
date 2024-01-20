# eda_mds

Basic EDA functions implemented to improve on core Pandas DataFrame functions 

## Installation

This project has not yet been uploaded to PyPI. 
Please see [CONTRIBUTING.md] for instructions to install locally. 

## Summary

This package is created for kick-starting EDA stage of a machine learning and analytics projects. It's primary objective
is to improve upon the popular EDA functions present in pandas package. There are 4 functions that deliver insights and
identify potential problems in the dataset. Four functions and their descriptions can be found
in [Function Descriptions](#Function Descriptions)

### Function Descriptions

- cor_eda(): The function cor_eda accepts a dataset and isolates its numerical continuous variables. It calculates the
  correlation between each numerically continuous variable from scratch and displays the results in a table.
- info_na(): This function replicates and extends behaviour of pandas.DataFrame.info(). New information will consist of
  row-level summary statistics for null values to characterize dataframe structure.
- cat_var_stats(): This function creates summary statistics about categorical variables in the dataframe. Number of
  unique values, frequency of values and whether some categories should binned will be among the info that will be
  presented.
- describe_outliers():  Extends the functionality of pandas.Dataframe.describe() for numeric data by additionally
  providing a count of lower-tail and upper-tail outliers.

### Python Ecosystem Integration

Our functions are heavily inspired from pandas package for python. EDA functions such as pandas.Dataframe.info,
pandas.Dataframe.describe and pandas.Dataframe.corr are
recreated and improved upon in this package. Our functions also dependent on pandas.Dataframe object which is defined in
pandas python package.

Pandas package repo: https://github.com/pandas-dev/pandas

## Usage

- TODO

## Contributing

Package created by Koray Tecimer, Paolo De Lagrave-Codina, Nicole Bidwell, Simon Frew.

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code
of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`eda_mds` was created by Koray Tecimer, Paolo De Lagrave-Codina, Nicole Bidwell, Simon Frew. It is licensed under the
terms of the MIT license.

## Credits

`eda_mds` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and
the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
