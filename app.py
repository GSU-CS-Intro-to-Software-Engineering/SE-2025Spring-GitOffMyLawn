import flu_finder_src.utils.data_fetcher as data

# Fetch the data from CDC
data.download_csv()

# Create and display dataframe
df_sorted = data.get_sorted_dataframe()
print(df_sorted)