from eda_mds.cor_eda import cor_eda
import pandas as pd
import numpy as np

# testing that the corr function matches the cor_eda function
dfA = pd.DataFrame(
    data={
        "age": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
        "income": [
            32000,
            45000,
            50000,
            50000,
            600000,
            65000,
            70000,
            75000,
            80000,
            85000,
        ],
    }
)

assert np.allclose(
    dfA.corr(), cor_eda(dfA), atol=1e-8
), "The correlation matrices are not approximately equal"


# testing that the corr function matches the cor_eda function
def test_correlation_matrix():
    """
    Verify that the computed correlation matrix matches the expected values.
    """
    dfA = pd.DataFrame(
        data={
            "age": [25, 30, 35, 40, 45, 55, 60, 65, 70, 70],
            "income": [
                32000,
                45000,
                50000,
                50000,
                60000,
                65000,
                70000,
                75000,
                80000,
                85000,
            ],
        }
    )
    assert np.allclose(
        dfA.corr(), cor_eda(dfA), atol=1e-8
    ), "The correlation matrices are not approximately equal"


# testing that the cor_eda function works if there are None values
def test_na_val():
    """
    Verify that df with NA's give expected values.
    """
    dfA = pd.DataFrame(
        data={
            "age": [25, None, 35, 40, 45, 55, 60, None, 70, 70],
            "income": [
                32000,
                45000,
                50000,
                50000,
                60000,
                65000,
                70000,
                75000,
                80000,
                85000,
            ],
        }
    )
    dfB = pd.DataFrame(
        data={
            "age": [25, 35, 40, 45, 55, 60, 70, 70],
            "income": [
                32000,
                50000,
                50000,
                60000,
                65000,
                70000,
                80000,
                85000,
            ],
        }
    )
    assert np.allclose(
        cor_eda(dfB), cor_eda(dfA), atol=1e-8
    ), "The function default are correctly adjusting to NA rows"


# testing what happens if our data frame is all None
def test_na_val_all():
    """
    Verify that df with all NA's give expected values.
    """
    dfA = pd.DataFrame(
        data={
            "age": [None, None, None],
            "income": [
                None,
                None,
                None,
            ],
        }
    )
    result = cor_eda(dfA)
    assert (
        result == "There are no numerical columns"
    ), "The function indicated there are no numerical columns"


# testing what function will do if none of the values are num
def test_no_numerical_columns():
    """
    Verify that df has no numeric column it results in expected message.
    """
    df = pd.DataFrame({"category": ["A", "B", "C"], "boolean": [True, False, True]})

    result = cor_eda(df)
    assert (
        result == "no numerical columns found"
    ), "The function should indicate there are no numerical columns"


# testing what function handling a wrong input value
def test_na_handling_input():
    """
    Verify that df with na_handling with wrong input gives expected output.
    """
    df = pd.DataFrame({"category": [1, 2, 3], "boolean": [3, 3, 3]})
    try:
        cor_eda(df, na_handling="incorrect_value")
        assert False, "The function should have raised a ValueError"
    except ValueError as e:
        assert (
            str(e) == "na_handling must be 'drop', 'mean', 'median', or 'value'"
        ), "The function raised ValueError but with the incorrect message"


# testing that the df did not change after function was used
def test_df_notChanged():
    """
    Verify that df did not change after function is run.
    """
    df = pd.DataFrame({"category": [1, None, 3], "boolean": [3, 3, 3]})
    x = df.shape
    cor_eda(df, na_handling="mean")
    y = df.shape
    assert np.allclose(
        x, y, atol=1e-8
    ), "The data frame should not be changed by the function"


# testing function handles na_handling mean correctly
def test_na_handling_mean():
    """
    Verify that df with na_handling with mean input gives expected output.
    """
    dfA = pd.DataFrame(
        data={
            "age": [25, None, 35, 40, 45, 55, 60, None, 70, 70],
            "income": [
                32000,
                45000,
                50000,
                50000,
                60000,
                65000,
                70000,
                75000,
                80000,
                85000,
            ],
        }
    )
    age_mean = pd.Series([25, 35, 40, 45, 55, 60, 70, 70]).mean()

    dfB = pd.DataFrame(
        data={
            "age": [25, age_mean, 35, 40, 45, 55, 60, age_mean, 70, 70],
            "income": [
                32000,
                45000,
                50000,
                50000,
                60000,
                65000,
                70000,
                75000,
                80000,
                85000,
            ],
        }
    )
    assert np.allclose(
        cor_eda(dfB), cor_eda(dfA, na_handling="mean"), atol=1e-8
    ), "The function default are correctly adjusting to NA rows"
