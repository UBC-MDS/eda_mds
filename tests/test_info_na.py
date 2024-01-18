import pytest

import numpy as np
import pandas as pd

from eda_mds import info_na

np.random.seed = 1234


# Test for correct input types
def test_input_type():
    with pytest.raises(TypeError):
        info_na(12)


# Test to handle all-na values
def test_all_na():
    with pytest.warns(UserWarning):
        data, _ = generate_data(1)
        info_na(data)


# Test to handle no na values
def test_no_na():
    data, _ = generate_data(2)
    info_na(data)


# Test correct output
def test_output():
    data, response = generate_data(3)
    info_na(data)
# add correct output for the above examples
# add correct output expectation for randomly generated


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

    Returns
    -------
    tuple
        tuple of desired data to provide and expected response, if applicable.

    """

    if example == 1:
        data = pd.DataFrame([[np.nan, np.nan], [np.nan, np.nan]])
        response = None
    elif example == 2:
        data = pd.DataFrame([[1, 2], [4, 5]])
        response = None  # update to true value
    elif example == 3:
        data = pd.DataFrame(np.random.random((2000, 10)))
        data[
            np.hstack(
                (
                    np.random.random((2000, 1)) < 0.5,
                    np.random.random((2000, 4)) < 0.025,
                    np.random.random((2000, 5)) < 0.05,
                )
            ) == True
        ] = np.nan
        response = None  # update to true value

    return data, response


# tests
# 4. check print output is correct
