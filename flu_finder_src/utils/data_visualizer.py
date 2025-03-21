import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
from data_fetcher import get_sorted_dataframe
from queries import *

df = get_sorted_dataframe()
# #! Make sure you replace Ohio with sorted dataframe
# df = filter_by_state("Ohio")

def set_time_frame(start, end, *args):
    # Note: arguments not case-sensitive (.title())
    
    # Nation specific
    if len(args) < 1:
        national = get_time_frame(df, start, end)
        # print(tabulate(national, headers="keys", tablefmt="simple_outline"))
        return national
        
    # State specific
    elif len(args) == 1:
        # Made the name not case sensitive
        state = filter_by_state((args[0].title()))
        frame = get_time_frame(state, start, end)
        # print(tabulate(frame, headers="keys", tablefmt="simple_outline"))
        return frame
    # County specific
    elif len(args) > 1:
        county = filter_by_county((args[1].title()), (args[0].title()))
        frame = get_time_frame(county, start, end)
        # print(tabulate(frame, headers="keys", tablefmt="simple_outline"))
        return frame
        
    
def line_graph_maker(df, unit):
    # Unit displayed with x-axis tick mark spacing
    # TODO: Implement graph build
    xpoints = df["Outbreak Date"]
    ypoints = df["Flock Size"]
    plt.plot(xpoints, ypoints, linestyle = 'dotted', marker='o')
    plt.show()
    

#------------------------------------------- Method Testing -----------------------------------------#
if __name__ == "__main__":
    # set_time_frame("2025", "2030")                           # <== National
    # set_time_frame("2025-01-01", "2025-02-01", "Georgia")    # <== State
    frame = set_time_frame("2024", "2030", "ioWA", "BUENA VistA")    # <== County
    line_graph_maker(frame, "seconds")