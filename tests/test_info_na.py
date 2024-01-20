import pytest

import numpy as np
import pandas as pd

from eda_mds import info_na


def test_input_type():
    """Tests that info_na raises a TypeError when the input is not a pandas.DataFrame."""
    with pytest.raises(TypeError):
        info_na(12)


def test_all_na():
    """Test that info_na raises a UserWarning when the input dataframe has all null values."""
    with pytest.warns(UserWarning):
        data, _ = generate_data(1)
        info_na(data)


def test_no_na():
    """Test that no error is thrown when an input dataframe has no null values."""
    data, _ = generate_data(2)
    info_na(data)


def test_output(capsys):
    """
    Test that output printed by the function, its calculations, are correct.
    Note that the `capsys` is a `pytest` handler to capture console output.
    """
    with pytest.warns(UserWarning):
        data, response = generate_data(1)
        info_na(data)
        output = capsys.readouterr()
        assert output.out == response

    data, response = generate_data(2)
    info_na(data)
    output = capsys.readouterr()
    assert output.out == response

    data, response = generate_data(3)
    info_na(data)
    output = capsys.readouterr()
    assert output.out == response

    data, response = generate_data(4)
    info_na(data)
    output = capsys.readouterr()
    assert output.out == response


# Helper function
def generate_data(example):
    """Helper function to generate example data

    Parameters
    ----------
    example : int
        integer corresponding to example used:
        1 : all-na values
        2 : no na values
        3 : randomly generated data with NAs seeded
        4 : small pre-generated dataframe with strings

    Returns
    -------
    tuple
        tuple of desired data to provide (pandas.DataFrame) and expected response (string), if applicable.
    """

    if example == 1:
        data = pd.DataFrame([[np.nan, np.nan], [np.nan, np.nan]])
        response = """
type: <class 'pandas.core.frame.DataFrame'>
shape: (2, 2)
memory usage: 160 B
--------
columns:
 #  column  null count  null %   dtype
 0       0           2   100.0 float64
 1       1           2   100.0 float64
-----
rows:
total rows              2.0
any null count          2.0
any null %            100.0
all null count          2.0
all null %            100.0
mean null count         2.0
std.dev null count      0.0
max null count          2.0
min null count          2.0

"""

    elif example == 2:
        data = pd.DataFrame([[1, 2], [4, 5]])
        response = """
type: <class 'pandas.core.frame.DataFrame'>
shape: (2, 2)
memory usage: 160 B
--------
columns:
 #  column  null count  null % dtype
 0       0           0     0.0 int64
 1       1           0     0.0 int64
-----
rows:
total rows            2.0
any null count        0.0
any null %            0.0
all null count        0.0
all null %            0.0
mean null count       0.0
std.dev null count    0.0
max null count        0.0
min null count        0.0

"""

    elif example == 3:
        np.random.seed(1234)
        data = pd.DataFrame(np.random.random((2000, 10)))
        data[
            np.hstack(
                (
                    np.random.random((2000, 1)) < 0.5,
                    np.random.random((2000, 4)) < 0.025,
                    np.random.random((2000, 5)) < 0.05,
                )
            )
            == True
        ] = np.nan
        response = """
type: <class 'pandas.core.frame.DataFrame'>
shape: (2000, 10)
memory usage: 156.4 KB
--------
columns:
 #  column  null count  null %   dtype
 0       0        1010   50.50 float64
 1       1          60    3.00 float64
 2       2          44    2.20 float64
 3       3          51    2.55 float64
 4       4          45    2.25 float64
 5       5         102    5.10 float64
 6       6         114    5.70 float64
 7       7          96    4.80 float64
 8       8         101    5.05 float64
 9       9          83    4.15 float64
-----
rows:
total rows            2000.00
any null count        1283.00
any null %              64.15
all null count           0.00
all null %               0.00
mean null count          0.85
std.dev null count       0.77
max null count           4.00
min null count           0.00

"""

    elif example == 4:
        data = pd.DataFrame(
            [
                [np.nan, 13, "hello"],
                [np.nan, np.nan, "this"],
                [37, 45, "is"],
                [256, 31, ""],
                [1, np.nan, "test"],
            ],
            index=["First", "Second", "Third", "Fourth", "Fifth"],
            columns=["Column1", "ColumnNumber2", "Column3"],
        )
        response = """
type: <class 'pandas.core.frame.DataFrame'>
shape: (5, 3)
memory usage: 692 B
--------
columns:
 #        column  null count  null %   dtype
 0       Column1           2    40.0 float64
 1 ColumnNumber2           2    40.0 float64
 2       Column3           0     0.0  object
-----
rows:
total rows             5.00
any null count         3.00
any null %            60.00
all null count         0.00
all null %             0.00
mean null count        0.80
std.dev null count     0.84
max null count         2.00
min null count         0.00

"""

    return data, response
