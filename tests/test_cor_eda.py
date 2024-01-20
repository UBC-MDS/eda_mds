from eda_mds.cor_eda import cor_eda
import pandas as pd
import numpy as np

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


def test_correlation_matrix():
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


def test_na_val():
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


def test_na_val_all():
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


def test_no_numerical_columns():
    df = pd.DataFrame({"category": ["A", "B", "C"], "boolean": [True, False, True]})

    result = cor_eda(df)
    assert (
        result == "There are no numerical columns"
    ), "The function should indicate there are no numerical columns"


def test_na_handling_input():
    df = pd.DataFrame({"category": [1, 2, 3], "boolean": [3, 3, 3]})
    try:
        cor_eda(df, na_handling="incorrect_value")
        assert False, "The function should have raised a ValueError"
    except ValueError as e:
        assert (
            str(e) == "na_handling must be 'drop', 'mean', 'median', or 'value'"
        ), "The function raised ValueError but with the incorrect message"


def test_df_notChanged():
    df = pd.DataFrame({"category": [1, None, 3], "boolean": [3, 3, 3]})
    x = df.shape
    cor_eda(df, na_handling="mean")
    y = df.shape
    assert np.allclose(
        x, y, atol=1e-8
    ), "The data frame should not be changed by the function"


def test_na_handling_mean():
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