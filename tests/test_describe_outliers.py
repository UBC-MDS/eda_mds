import pandas as pd
import numpy as np
import pytest

from eda_mds.describe_outliers import describe_outliers

df = pd.DataFrame({
    'A': [-3, 0, 1, 2, 3, 10, 3],
    'B': [4, np.nan , 6, -10, 1, 1, 3],
    'C': [1, 7, 8, 9, -1000, 3, 3], 
    'D': ['a', 'b','c', 'd', 'e', 'g', 'h']
})

df_no_numeric = pd.DataFrame({
    'A': ['a', 'b','c', 'd', 'e', 'g', 'h'], 
    'B': ['3', '2','1', '5', '3', '4', '3']
})

def test_threshold_value():
    with pytest.raises(ValueError):
        describe_outliers(df, threshold=-2)    
    
    with pytest.raises(ValueError):
        describe_outliers(df, threshold=-3.5)
    
def test_df_numeric():
    with pytest.raises(ValueError):
        describe_outliers(df_no_numeric)

def test_df_type():
    with pytest.raises(TypeError):
        describe_outliers(np.array([1, 2, 3]))
    
    with pytest.raises(TypeError):
        describe_outliers(df = 4, threshold=3)

def test_output_values():    
    assert describe_outliers(df).iloc[1].iloc[1] == 6
    assert describe_outliers(df).iloc[2].iloc[1] == 0.8333333333333334
    assert describe_outliers(df).iloc[3].iloc[1] == 5.636192568273964
    assert describe_outliers(df).iloc[4].iloc[1] == -10.0
    assert describe_outliers(df).iloc[5].iloc[1] == 1.0
    assert describe_outliers(df).iloc[6].iloc[1] == 2.0
    assert describe_outliers(df).iloc[7].iloc[1] == 3.75
    assert describe_outliers(df).iloc[8].iloc[1] == 6.0
    assert describe_outliers(df).iloc[9].iloc[1] == 1.0
    assert describe_outliers(df).iloc[10].iloc[1] == 0.0


