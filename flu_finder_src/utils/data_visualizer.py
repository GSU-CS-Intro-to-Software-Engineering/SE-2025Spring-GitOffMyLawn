import pandas as pd
import plotly.express as px
from data_fetcher import get_sorted_dataframe, get_reversed_dataframe
from queries import *

#! Replace this with db_methods
df = get_sorted_dataframe()


def bar_graph_maker(df, output_file="outbreak_plot.html"):
    if df.empty:
        print("No data to plot. Check your date range and filters.")
        return

    df = df.copy()
    df["Outbreak Date"] = pd.to_datetime(df["Outbreak Date"])

    fig = px.bar(
        df,
        x="Outbreak Date",
        y="Flock Size",
        title="Outbreak Flock Size Over Time",
        labels={"Outbreak Date": "Outbreak Date", "Flock Size": "Flock Size"},
        color_discrete_sequence=["dodgerblue"]
    )

    # Tooltip formatting (optional customization)
    fig.update_traces(
        marker=dict(color='blue', line=dict(width=1, color='black')),
        hovertemplate="Date: %{x|%m-%d-%Y}<br>Size: %{y:,}"
    )

    # Improve layout
    fig.update_layout(
        xaxis_title="Outbreak Date",
        yaxis_title="Flock Size",
        title_x=0.5,
        hoverlabel=dict(bgcolor="white", font_size=12),
        template="plotly_white",
        dragmode="pan",
        bargap=0.1
    )
    
    # Scroll wheel zoom and always visible modebar
    config = {"displayModeBar": True,
              "scrollZoom": True,
              "modeBarButtonsToRemove": ["autoScale", "select2d", "lasso2d"]}

    # Save to HTML
    fig.write_html(output_file, config=config)
    print(f"Plot saved to {output_file}")



def line_graph_maker(df, output_file="outbreak_plot.html"):
    if df.empty:
        print("No data to plot. Check your date range and filters.")
        return

    df = df.copy()
    df["Outbreak Date"] = pd.to_datetime(df["Outbreak Date"])

    fig = px.line(
        df,
        x="Outbreak Date",
        y="Flock Size",
        title="Outbreak Flock Size Over Time",
        markers=True,
        labels={"Outbreak Date": "Outbreak Date", "Flock Size": "Flock Size"},
        color_discrete_sequence=["dodgerblue"]
    )

    # Tooltip formatting (optional customization)
    fig.update_traces(
        marker=dict(size=6, color='blue', line=dict(width=1, color='black')),
        hovertemplate="Date: %{x|%m-%d-%Y}<br>Size: %{y:,}"
    )

    # Improve layout
    fig.update_layout(
        xaxis_title="Outbreak Date",
        yaxis_title="Flock Size",
        title_x=0.5,
        hoverlabel=dict(bgcolor="white", font_size=12),
        template="plotly_white",
        dragmode="pan"
    )
    
    # Scroll wheel zoom and always visible modebar
    config = {"displayModeBar": True,
              "scrollZoom": True,
              "modeBarButtonsToRemove": ["autoScale", "select2d", "lasso2d"]}

    # Save to HTML
    fig.write_html(output_file, config=config)
    print(f"Plot saved to {output_file}")


#------------------------------------------- Method Testing -----------------------------------------#
if __name__ == "__main__":
    frame = get_time_frame_by_location("2022", "2030")                           # <== National
    # frame = get_time_frame_by_location("2025-01-01", "2025-02-01", "Georgia")    # <== State
    # frame = get_time_frame_by_location("2024", "2030", "ioWA", "BUENA VistA")    # <== County
    # summed_frame = sum_by_date(frame)
    # bar_graph_maker(summed_frame)
    # line_graph_maker(summed_frame)
    
    # TEST: sum in given time frame
    # frame = get_time_frame_by_location("2025-01-13", "2025-01-14")
    # print(sum_by_date(frame))
