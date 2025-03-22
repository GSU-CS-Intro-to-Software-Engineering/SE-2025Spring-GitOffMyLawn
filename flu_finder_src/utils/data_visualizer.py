import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplcursors
import mpld3
from data_fetcher import get_sorted_dataframe
from queries import *

df = get_sorted_dataframe()
df_summed = sum_by_date(df)

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

def line_graph_maker(df):
    if df.empty:
        print("No data to plot. Check your date range and filters.")
        return

    df = df.copy()
    df["Outbreak Date"] = pd.to_datetime(df["Outbreak Date"], errors='coerce')

    # fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    fig, ax = plt.subplots(figsize=(10, 6), dpi=65)

    # Plot data + lines
    ax.plot(df["Outbreak Date"], df["Flock Size"], linestyle='-', marker='o', markersize=5, markerfacecolor='blue', markeredgecolor='black', linewidth=2, color='dodgerblue', alpha=0.9)
    
    # Scatter only for points (used by mplcursors)
    scatter = ax.scatter(df["Outbreak Date"], df["Flock Size"], cmap='coolwarm', edgecolor='black', zorder=3)

    # Format x-axis (dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xticks(rotation=45, ha="right")

    # Turn off scientific notation for y-axis
    ax.ticklabel_format(style='plain', axis='y')

    # Labels and title
    ax.set_xlabel("Outbreak Date")
    ax.set_ylabel("Flock Size")
    ax.set_title("Outbreak Flock Size Over Time")

    # Add grid for readability
    ax.grid(True, linestyle="--", alpha=0.6)

    def format_coord(x, y):
        return f"(x, y) = ({mdates.num2date(x).strftime('%m-%d-%Y')}, {y:,.0f})"
    
    # Override default tooltip format (no scientific notation)
    ax.format_coord = format_coord
    
    cursor = mplcursors.cursor(scatter, hover=mplcursors.HoverMode(2))
    @cursor.connect("add")
    def on_add(sel):
        x = mdates.num2date(sel.target[0]).strftime('%m-%d-%Y')
        y = f"{sel.target[1]:,.0f}"
        sel.annotation.set_text(f"Date: {x}\n Size:{y}")

        # Style the annotation box
        sel.annotation.get_bbox_patch().set(fc="white", ec="black", alpha=0.85, boxstyle="round,pad=0.5")
        sel.annotation.get_bbox_patch().set_linewidth(1)

        # Style the text
        sel.annotation.set_fontsize(10)
        
        # Remove the arrow
        sel.annotation.arrow_patch.set_visible(False)
        sel.annotation.set_visible(True)
        
        # Dynamic color changes, changes box color depending on flock size (optional)
        # if sel.target[1] > 500000:
        #     sel.annotation.get_bbox_patch().set(fc="lightcoral")
        # else:
        #     sel.annotation.get_bbox_patch().set(fc="lightgreen")
        
        


    plt.tight_layout()
    # plt.show()
    mpld3.show(fig)
    

#------------------------------------------- Method Testing -----------------------------------------#
if __name__ == "__main__":
    frame = set_time_frame("2022", "2030")                           # <== National
    # frame = set_time_frame("2025-01-01", "2025-02-01", "Georgia")    # <== State
    # frame = set_time_frame("2024", "2030", "ioWA", "BUENA VistA")    # <== County
    summed_frame = sum_by_date(frame)
    line_graph_maker(summed_frame)
    
    # TEST: sum in given time frame
    # frame = set_time_frame("2025-01-13", "2025-01-14")
    # print(sum_by_date(frame))
    # print(tabulate(frame, headers="keys", tablefmt="simple_outline"))
