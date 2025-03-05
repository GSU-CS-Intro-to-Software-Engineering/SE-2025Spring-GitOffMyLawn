from data_fetcher import get_dataframe
import polars as pl

df = get_dataframe()

# -------------------------------------  State Methods -----------------------------------------------#
# Filter Cases by State
def filter_by_state(state: str):
    return df.filter(pl.col("State") == state)

# Get total number of outbreaks per state
def total_outbreaks_by_state(state: str):
    return filter_by_state(state).height

# Get total flock size by state
def total_flock_size_by_state(state: str):
    return filter_by_state(state)["Flock Size"].cast(int).sum()

# Get Summary for State
def get_state_summary(state: str):
    outbreaks = total_outbreaks_by_state(state)
    flock_size = total_flock_size_by_state(state)
    return f"{state}: {outbreaks} outbreaks, {flock_size} total flock affected."

# -------------------------------------  Country Methods -----------------------------------------------#
def get_country_summary():
    total_outbreaks = df.height
    total_flock_size = df["Flock Size"].cast(int).sum()
    return f"Total outbreaks in the country: {total_outbreaks}, Total flock affected: {total_flock_size}"

# ------------------------------------- Method Testing -----------------------------------------------#
# print(filter_by_state("Georgia"))
# print(total_outbreaks_by_state("Georgia"))
# print(total_flock_size_by_state("Georgia"))
# print(get_state_summary("Georgia"))
# print(get_country_summary())
