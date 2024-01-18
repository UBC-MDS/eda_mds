import os
import sys
import pytest

import numpy as np
import pandas as pd

from eda_mds import info_na


# Test for correct input types
def test_input_type():
    with pytest.raises(TypeError):
        info_na(12)


# Test to handle all-na values
def test_all_na():
    with pytest.warns(UserWarning):
        info_na(pd.DataFrame([[np.nan, np.nan], [np.nan, np.nan]]))


# Test to handle no na values
def test_no_na():
    info_na(pd.DataFrame([[1, 2], [4, 5]]))

# Test correct output
# def test_output():
    # add correct output for the above examples
    # add correct output expectation for randomly generated 


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
    
    return data, response

# tests
# 4. check print output is correct
