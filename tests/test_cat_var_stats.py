import pytest
import io
import pandas as pd
import numpy as np
from contextlib import redirect_stdout
from src.eda_mds.cat_var_stats import cat_var_stats


def test_non_dataframe_input():
    """Tests if function raises TypeError if user input something other than a Pandas.DataFrame"""
    with pytest.raises(TypeError):
        cat_var_stats('not a dataframe')


def test_non_numeric_threshold():
    """Tests if function raises TypeError if user input something other than a number for threshold parameter"""
    df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'col2': ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b']})
    with pytest.raises(TypeError):
        cat_var_stats(df, 'not a number')


def test_wrong_threshold():
    """Tests if function raises ValueError if user input a threshold value that is too large or too small"""
    df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'col2': ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b']})
    threshold = -1
    threshold2 = 101
    with pytest.raises(ValueError):
        cat_var_stats(df, threshold)
        cat_var_stats(df, threshold2)


def test_empty_dataframe():
    """Tests if function raises ValueError if user input an empty pandas.DataFrame"""
    df = pd.DataFrame({'col1': [], 'col2': []})
    df2 = pd.DataFrame({})
    with pytest.raises(ValueError):
        cat_var_stats(df)
        cat_var_stats(df2)


def test_func_output():
    """Tests if function outputs the correct console output"""
    # goose and bear are below the threshold there should be a binning recommendation for the two.
    cat_col = ['dog', 'cat', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat',
               'dog', 'cat', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat',
               'dog', 'cat', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat',
               'dog', 'cat', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat',
               'dog', 'cat', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat',
               'dog', 'cat', 'cat', 'dog', 'cat', 'dog', 'cat', 'dog', 'cat',
               'dog', 'cat', 'cat', 'goose', 'bear']

    # Java is only value below the threshold. There should be no recommendation
    cat_col2 = ['python', 'R', 'R', 'python', 'R', 'python', 'R', 'python', 'R',
                'python', 'R', 'R', 'python', 'R', 'python', 'R', 'python', 'R',
                'python', 'R', 'R', 'python', 'R', 'python', 'R', 'python', 'R',
                'python', 'R', 'R', 'python', 'R', 'python', 'R', 'python', 'R',
                'python', 'R', 'R', 'python', 'R', 'python', 'R', 'python', 'R',
                'python', 'R', 'R', 'python', 'R', 'python', 'R', 'python', np.NaN,
                'python', 'R', 'R', 'Java', 'Java']

    df = pd.DataFrame({'numeric_col': np.arange(0, len(cat_col), 1),
                       'cat_col_1': cat_col,
                       'text_col': [str(i) for i in range(len(cat_col))],
                       'cat_col_2': cat_col2})

    correct_output = """Column: cat_col_1
Number of unique values: 4
Frequency of values:
dog: 42.37%
cat: 54.24%
goose: 1.69%
bear: 1.69%
Binning recommendations:
goose, bear values can be binned into "other" category as they are lower than binning threshold
------------------------------------


Column: cat_col_2
Number of unique values: 3
Frequency of values:
python: 42.37%
R: 52.54%
nan: 1.69%
Java: 3.39%
Binning recommendations:
nan, Java values can be binned into "other" category as they are lower than binning threshold
------------------------------------


"""
    f = io.StringIO()
    with redirect_stdout(f):
        cat_var_stats(df, 5)
    output = f.getvalue()
    assert output == correct_output
