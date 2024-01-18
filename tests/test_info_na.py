import os
import sys
import pytest

import numpy as np
import pandas as pd

from eda_mds import info_na


def test_input_type():
    with pytest.raises(TypeError):
        info_na(12)

def test_all_na():
    with pytest.raises(Warning):
        info_na(
            pd.DataFrame(
                [[np.nan, np.nan], [np.nan, np.nan]]
            )
        )

# tests
# 1. is it a dataframe? 
# 2. a seperate check for all na df
# 3. check print output is correct
# 4. verbose flag, gives dictionary? 
