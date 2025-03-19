import pandas as pd
from tabulate import tabulate
from data_fetcher import get_sorted_dataframe

df = get_sorted_dataframe()

#------------------------------------------- Country Methods -----------------------------------------#

# Get total outbreaks in the US
def total_outbreaks_USA():
    return len(df)

# Get total flock size in the US
def total_flock_size_USA():
    return df["Flock Size"].sum()

# Get summary for the US
def get_USA_summary():
    total_outbreaks = total_outbreaks_USA()
    total_flock_size = total_flock_size_USA()
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


#------------------------------------------- Method Testing -----------------------------------------#
if __name__ == "__main__":
    # --- COUNTRY METHODS ---
    # print(tabulate(df, headers="keys", tablefmt="simple_outline"))
    # print(total_outbreaks_USA())
    # print(total_flock_size_USA())
    print(get_USA_summary())
    
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