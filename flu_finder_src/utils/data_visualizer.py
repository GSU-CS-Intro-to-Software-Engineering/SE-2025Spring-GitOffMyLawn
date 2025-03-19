# import polars as pl
# import matplotlib.pyplot as plt, mpld3
# import matplotlib.dates as mdates
# from mpld3 import plugins
# # from data_fetcher import get_sorted_dataframe
# from queries import *

# # df = get_sorted_dataframe()
# df = filter_by_state("Ohio")

# fig, ax = plt.subplots(figsize=(10,6), dpi=50)
# ax.scatter(
#     x=df["Outbreak Date"],
#     y=df["Flock Size"]
# )
# ax.set_title("Number of Outbreaks Over Time")
# ax.set_xlabel("Outbreak Date")
# ax.set_ylabel("Flock Size")

# ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d, %Y"))

# # plt.ticklabel_format(style="plain")

# # # Enable mpld3's scroll functionality by default
# # mpld3.plugins.clear(fig)
# plugins.connect(fig, plugins.Reset(), plugins.Zoom(enabled=True), plugins.BoxZoom(enabled=True), plugins.MousePosition())


# # # Creates html of the graph
# mpld3.save_html(fig=fig, fileobj="output.html")

import polars as pl
import matplotlib.pyplot as plt, mpld3
import matplotlib.dates as mdates
from mpld3 import plugins
from queries import *

# df = get_sorted_dataframe()
df = filter_by_state("Ohio")

# Convert "Outbreak Date" to datetime format
df = df.with_columns(pl.col("Outbreak Date").str.strptime(pl.Date, "%m/%d/%Y"))

fig, ax = plt.subplots(figsize=(30, 18), dpi=20)

# Plot using NumPy arrays (no Pandas needed)
ax.scatter(
    x=df["Outbreak Date"].to_numpy(),  
    y=df["Flock Size"].to_numpy()
)

ax.set_title("Number of Outbreaks Over Time")
ax.set_xlabel("Outbreak Date")
ax.set_ylabel("Flock Size")

# Improve date formatting
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # Show every 3 months
ax.xaxis.set_minor_locator(mdates.MonthLocator(interval=1))  # Minor ticks every month
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))  # Example: "Apr 2023"
fig.autofmt_xdate()  # Rotate for better readability

# Prevent scientific notation on the y-axis
ax.yaxis.set_major_formatter(plt.ScalarFormatter())
ax.ticklabel_format(style="plain", axis="y")  # Prevent scientific notation

# Enable mpld3's scroll functionality by default
mpld3.plugins.clear(fig)
plugins.connect(fig, plugins.Reset(), plugins.Zoom(enabled=True), plugins.BoxZoom(enabled=True), plugins.MousePosition())

# Creates HTML of the graph
mpld3.save_html(fig=fig, fileobj="output.html")

