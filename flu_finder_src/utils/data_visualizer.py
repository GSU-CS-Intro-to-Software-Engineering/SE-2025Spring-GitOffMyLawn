import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from data_fetcher import get_sorted_dataframe
from queries import *

df = get_sorted_dataframe()
# #! Make sure you replace Ohio with sorted dataframe
# df = filter_by_state("Ohio")

def line_graph_maker(start, end, unit, *args):
    # Note: arguments not case-sensitive (.title())
    
    # Nation specific
    if len(args) < 1:
        national = get_time_frame(df, start, end)
        print(tabulate(national, headers="keys", tablefmt="simple_outline"))
        # Unit displayed with x-axis tick mark spacing
        # TODO: Implement graph build
        
    # State specific
    elif len(args) == 1:
        # Made the name not case sensitive
        state = filter_by_state((args[0].title()))
        frame = get_time_frame(state, start, end)
        print(tabulate(frame, headers="keys", tablefmt="simple_outline"))
        # Unit displayed with x-axis tick mark spacing
        # TODO: Implement graph build
    # County specific
    elif len(args) > 1:
        county = filter_by_county((args[1].title()), (args[0].title()))
        print(tabulate(county, headers="keys", tablefmt="simple_outline"))
        # Unit displayed with x-axis tick mark spacing
        # TODO: Implement graph build
    

#------------------------------------------- Method Testing -----------------------------------------#
if __name__ == "__main__":
    # line_graph_maker("2025", "2030", "seconds")
    # line_graph_maker("2025-01-01", "2025-02-01", "seconds", "Georgia")
    line_graph_maker("2020", "2030", "seconds", "ioWA", "BUENA VistA")