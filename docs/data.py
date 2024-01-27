import pandas as pd
from src.eda_mds.cat_var_stats import cat_var_stats
from eda_mds.cor_eda import cor_eda
from eda_mds import info_na
from eda_mds.describe_outliers import describe_outliers



df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')


#print(cor_eda(df, na_handling="drop"))
cat_var_stats(df)