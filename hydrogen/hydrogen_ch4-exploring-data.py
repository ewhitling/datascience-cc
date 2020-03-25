# %% codecell
import pandas as pd
import sqlite3

# connect to the dataset
myDB = './data/cephalopod_RnD.db'
connection = sqlite3.connect(myDB)

# read the data into a dataframe
mySQL = "SELECT * FROM spady_defense"
df = pd.read_sql(mySQL, connection)
# %% codecell
# how many records?
len(df)
# %% codecell
# print the top of the dataframe
df.head(10)
# %% codecell
# print the tail
df.tail()
# %% codecell
# what are the datatypes?
print(df.dtypes)
# %% codecell
# print the a random middlish row
print(df.loc[[44]])
# %% codecell
print(df.loc[44])
# %% codecell
print(df.loc[44:50])
# %% codecell
# An error! Let's force the string: n/a into a NaN
df['TimetoReact'] = pd.to_numeric(df['TimetoReact'], errors='coerce')
print(df.dtypes)
# %% codecell
# lets go back to our strings
# Treatment    Active    ReactionType    InkDischarge    BodyPattern
# field8    field9    field10    field11    field12

# first lets see if anything exists in the field columns
pd.notna(df['field8'])

# %% codecell
# check again, using an aggregate
pd.notna(df['field8']).sum()
# %% codecell
# check another way
df['field9'].unique().tolist()
# %% codecell
# much more efficent way to check.
df[['field8', 'field9', 'field10', 'field11', 'field12']].drop_duplicates()
# %% codecell
# remove the extra columns
# from pandas documentation:
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
# -- axis : {0 or ‘index’, 1 or ‘columns’}, default 0
# ---- Whether to drop labels from the index (0 or ‘index’) or columns (1 or ‘columns’).
df.drop(['field8', 'field9', 'field10', 'field11', 'field12'], axis=1, inplace=True)
# %% codecell
# get an overview of our numeric data
df.describe()
# %% codecell
na_lc = pd.isna(df['LineCrosses']).sum()
na_rt = pd.isna(df['TimetoReact']).sum()

print("the number of nulls in line crosses: %s" % na_lc)
print("the number of nulls in time to react: %s" % na_rt)
# %% codecell
# check the other columns
# Treatment    Active    ReactionType    InkDischarge    BodyPattern
for column in df.select_dtypes(include=object).keys():
    print("-----")
    print("Value counts in: %s" % column)
    print(df[column].value_counts())
    print("\n")
# %% codecell
df.select_dtypes(include=object)
# %% codecell
# visualize Line Crosses
df["LineCrosses"].plot.hist()
# %% codecell
# visualize Time to React
df["TimetoReact"].plot.hist()
# %% codecell
import seaborn as sns

sns.set(rc={'figure.figsize':(9, 7)})
sns.boxplot(
        x="LineCrosses",
        y="Treatment",
        data=df,
        palette="vlag")
# %% codecell
sns.boxplot(
        x="TimetoReact",
        y="Treatment",
        data=df,
        whis="range",
        palette="vlag")
# %% codecell
sns.countplot(x="Treatment", hue="InkDischarge", data=df)
# %% codecell
sns.countplot(x="Treatment", hue="ReactionType", data=df)
# %% codecell
sns.countplot(x="Treatment", hue="BodyPattern", data=df)
# %% codecell
