# import polars as pl
# import matplotlib.pyplot as plt, mpld3
# # import matplotlib.dates as mdates
# from matplotlib.dates import MonthLocator, DateFormatter
# from mpld3 import plugins
# # from data_fetcher import get_sorted_dataframe
# from queries import *

# # df = get_sorted_dataframe()
# #! Make sure you replace Ohio with sorted dataframe
# df = filter_by_state("Ohio")

# df = df.with_columns(pl.col("Outbreak Date").str.strptime(pl.Date, "%m/%d/%Y"))

# fig, ax = plt.subplots(figsize=(10,6), dpi=50)
# ax.scatter(
#     x=df["Outbreak Date"],
#     y=df["Flock Size"]
# )
# ax.set_title("Number of Outbreaks Over Time")
# ax.set_xlabel("Outbreak Date")
# ax.set_ylabel("Flock Size")

# # Sets the default position to years (ticks separated every 3 months)
# ax.xaxis.set_major_locator(MonthLocator(bymonth=[1,4,7,10]))
# ax.xaxis.set_major_formatter(DateFormatter('%m/%Y'))
# fig.autofmt_xdate()

# # plt.ticklabel_format(style="plain")

# # Enable mpld3's scroll functionality by default
# mpld3.plugins.clear(fig)
# plugins.connect(fig, plugins.Reset(), plugins.MousePosition())


# # Creates html of the graph
# mpld3.save_html(fig=fig, fileobj="output.html")

