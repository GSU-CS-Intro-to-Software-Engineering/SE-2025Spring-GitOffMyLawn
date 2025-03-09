import flu_finder_src.utils.data_fetcher as data
import polars as pl

# Fetch the data from CDC
data.download_csv()

# Create and display dataframe
df_sorted = data.get_sorted_dataframe()

# print(df_sorted)

# NOTE: Delete this once Sydney's find_case method is working 
row = df_sorted.filter(pl.col("index") == 0)
print(row)