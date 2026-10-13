import pandas as pd

# load the book sales dataset
df = pd.read_csv("data/book_sales.csv")

# check the number of rows and columns
print("\n--- dataset shape ---")
print(df.shape)

# display the first five rows
print("\n--- first five rows ---")
print(df.head())

# display the column names
print("\n--- column names ---")
print(df.columns.tolist())

# check the data types
print("\n--- data types ---")
print(df.dtypes)

# check missing values
print("\n--- missing values ---")
print(df.isna().sum())

# check numerical values
print("\n--- numerical summary ---")
print(df.describe())

# check duplicate rows
print("\n--- duplicate rows ---")
print(df.duplicated().sum())

# check unique values in each column
print("\n--- unique values ---")
print(df.nunique())






# inspect the categories and numerical ranges
print("\n--- genre categories ---")
print(df["genre"].value_counts(dropna=False))

print("\n--- language categories ---")
print(df["language_code"].value_counts(dropna=False))

print("\n--- author rating categories ---")
print(df["Author_Rating"].value_counts(dropna=False))

print("\n--- book rating range ---")
print(df["Book_average_rating"].min(), df["Book_average_rating"].max())

print("\n--- book ratings count range ---")
print(df["Book_ratings_count"].min(), df["Book_ratings_count"].max())

print("\n--- publishing year values that need checking ---")
print(df.loc[df["Publishing Year"].isna() | (df["Publishing Year"] < 0),
             ["Book Name", "Publishing Year"]])
