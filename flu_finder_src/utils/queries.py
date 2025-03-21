import pandas as pd
from tabulate import tabulate
from data_fetcher import get_sorted_dataframe

df = get_sorted_dataframe()

#------------------------------------------- National Methods -----------------------------------------#

# Get total outbreaks in the US
def total_outbreaks_national():
    return len(df)

# Get total flock size in the US
def total_flock_size_national():
    return df["Flock Size"].sum()

# Get summary for the US
def get_national_summary():
    total_outbreaks = total_outbreaks_national()
    total_flock_size = total_flock_size_national()
    return {
        "outbreaks": f"{total_outbreaks:,}",
        "flock_size": f"{total_flock_size:,}"
    }

#------------------------------------------- State Methods -----------------------------------------#
# Filter cases by State
def filter_by_state(state: str):
    return df[df["State"] == state]

# Get total outbreaks by State
def total_outbreaks_by_state(state: str):
    return len(filter_by_state(state))

# Get total flock size by State
def total_flock_size_by_state(state: str):
    return filter_by_state(state)["Flock Size"].sum()

# Get summary for State
def get_state_summary(state: str):
    outbreaks = total_outbreaks_by_state(state)
    flock_size = total_flock_size_by_state(state)
    return {
        "outbreaks": f"{outbreaks:,}",
        "flock_size": f"{flock_size:,}"
    }

#------------------------------------------- County Methods -----------------------------------------#
# Filter cases by County
def filter_by_county(county: str, state: str):
    return df[(df["County"] == county) & (df["State"] == state)]


# Get total outbreaks by County
def total_outbreaks_by_county(county: str, state: str):
    return len(filter_by_county(county, state))

# Get total flock size by County
def total_flock_size_by_county(county: str, state: str):
    return filter_by_county(county, state)["Flock Size"].sum()

# Get summary for County
def get_county_summary(county: str, state: str):
    outbreaks = total_outbreaks_by_county(county, state)
    flock_size = total_flock_size_by_county(county, state)
    return {
        "outbreaks": f"{outbreaks:,}",
        "flock_size": f"{flock_size:,}"
    }

#------------------------------------------- General Methods -----------------------------------------#
# Find values in a given a date range (df can be a subset of the full dataframe)
# Note: to get the full frame, either use the filter_by_ method, or set the start year to 1000 and the end year to 4000
# You also don't need specific dates. You can just input the year (ex: start=2025, end=2026 returns from start of 2025)
def get_time_frame(df, start, end):
    df = df.copy()
    df["Outbreak Date"] = pd.to_datetime(df["Outbreak Date"])
    mask = (df['Outbreak Date'] >= start) & (df['Outbreak Date'] <= end)
    return df.loc[mask]

#------------------------------------------- Method Testing -----------------------------------------#
if __name__ == "__main__":
    # --- COUNTRY METHODS ---
    print(tabulate(df, headers="keys", tablefmt="simple_outline"))
    # print(total_outbreaks_national())
    # print(total_flock_size_national())
    # print(get_national_summary())
    
    # --- STATE METHODS ---
    # print(tabulate(filter_by_state("Georgia"), headers="keys", tablefmt="simple_outline"))
    # print(total_outbreaks_by_state("Georgia"))
    # print(total_flock_size_by_state("Georgia"))
    # print(get_state_summary("Georgia"))
    
    # --- COUNTY METHODS ---
    # print(tabulate(filter_by_county("Elbert", "Georgia"), headers="keys", tablefmt="simple_outline"))
    # print(total_outbreaks_by_county("Elbert", "Georgia"))
    # print(total_flock_size_by_county("Elbert", "Georgia"))
    # print(get_county_summary("Elbert", "Georgia"))
    
    # --- GENERAL METHODS ---
    # print(tabulate(get_time_frame(df, "03/01/2025", "03/21/2025"), headers="keys", tablefmt="simple_outline"))