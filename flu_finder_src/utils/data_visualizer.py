import polars as pl
# import matplotlib.pyplot as plt
from data_fetcher import get_sorted_dataframe

df = get_sorted_dataframe()
df = df[-10:]

# fig, ax = plt.subplots()
# ax.scatter(
#     x=df["Outbreak Date"],
#     y=df["Flock Size"]
# )
# ax.set_title("Number of Outbreaks Over Time")
# ax.set_xlabel("Outbreak Date")
# ax.set_ylabel("Flock Size")

# # Creates html of the graph
# plt.savefig('output_name.png', bbox_inches='tight')