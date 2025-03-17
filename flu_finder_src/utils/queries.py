import polars as pl
from flu_finder_src.utils.data_fetcher import get_sorted_dataframe

df = get_sorted_dataframe()

#------------------------------------------- State Methods -----------------------------------------#
# Filter cases by State
def filter_by_state(state: str):
    return df.filter(pl.col("State") == state)

# Get total outbreaks by State
def total_outbreaks_by_state(state: str):
    return filter_by_state(state).height

# Get total flock size by State
def total_flock_size_by_state(state: str):
    return filter_by_state(state)["Flock Size"].cast(int).sum()

# Get summary for State
def get_state_summary(state: str):
    outbreaks = total_outbreaks_by_state(state)
    flock_size = total_flock_size_by_state(state)
    return {
        "outbreaks": outbreaks,
        "flock_size": flock_size
    }

 #------------------------------------------- County Methods -----------------------------------------#
 # Filter cases by County
def filter_by_county(county: str, state: str):
    return df.filter(pl.col("County") == county, pl.col("State") == state)

# Get total outbreaks by County
def total_outbreaks_by_county(county: str, state: str):
    return filter_by_county(county, state).height

# Get total flock size by County
def total_flock_size_by_county(county: str, state: str):
    return filter_by_county(county, state)["Flock Size"].cast(int).sum()

# Get summary for County
def get_county_summary(county: str, state: str):
    outbreaks = total_outbreaks_by_county(county, state)
    flock_size = total_flock_size_by_county(county, state)
    return {
        "outbreaks": outbreaks,
        "flock_size": flock_size
    }

#------------------------------------------- Country Methods -----------------------------------------#
# Get summary for Country
def get_country_summary():
    total_outbreaks = df.height
    total_flock_size = df["Flock Size"].cast(int).sum()
    return {
        "outbreaks": total_outbreaks,
        "flock_size": total_flock_size
    }

#------------------------------------------- Method Testing -----------------------------------------#
if __name__ == "__main__":
    print(filter_by_state("Georgia"))
    # print(total_outbreaks_by_state("Georgia"))
    # print(total_flock_size_by_state("Georgia"))
    # print(get_state_summary("Georgia"))
    # print(get_country_summary())
