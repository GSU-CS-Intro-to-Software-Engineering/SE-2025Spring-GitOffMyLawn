import pandas as pd
import plotly.express as px
# from data_fetcher import get_sorted_dataframe, get_reversed_dataframe
from db_methods import *
from queries import *

df = get_db()
def get_horizontal_comparison(df, *args, title=None, output_file="horizontal_comparison.html"):
    if df.empty:
        print("No data to visualize.")
        return

    df = df.copy()

    if len(args) == 0:
        # National level: group by state
        group_col = "State"
        scope_name = "USA"
    elif len(args) == 1:
        # State level: group by county
        group_col = "County"
        scope_name = args[0].title()
        df = df[df["State"].str.title() == scope_name]
    else:
        raise ValueError("Only 0 or 1 argument allowed (for national or state-level comparison)")

    # Group and calculate percentage
    grouped = df[group_col].value_counts().reset_index()
    grouped.columns = [group_col, "Outbreak Count"]
    grouped["Percentage"] = grouped["Outbreak Count"] / grouped["Outbreak Count"].sum() * 100

    # Sort from highest to lowest and reverse y-axis later for top-to-bottom effect
    grouped = grouped.sort_values(by="Percentage", ascending=False)

    if not title:
        title = f"Percent of Outbreaks by {group_col} – {scope_name}"

    fig = px.bar(
        grouped,
        x="Percentage",
        y=group_col,
        orientation='h',
        title=title,
        text="Percentage",
        color="Percentage",
        color_continuous_scale="RdYlGn_r"  # 🔁 'r' = reversed (so red = high, green = low)
    )

    fig.update_layout(
        xaxis_title="Percentage of Total Outbreaks",
        yaxis_title=group_col,
        title_x=0.5,
        template="plotly_white",
        yaxis=dict(autorange="reversed")  # ✅ largest on top
    )

    fig.update_traces(
        texttemplate='%{text:.2f}%',
        textposition='outside'
    )

    fig.write_html(output_file)
    print(f"Comparison chart saved to {output_file}")

def bar_graph_maker(df, output_file="outbreak_plot.html", title="Outbreaks Over Time"):
    if df.empty:
        print("No data to plot. Check your date range and filters.")
        return

    df = df.copy()
    df["Outbreak Date"] = pd.to_datetime(df["Outbreak Date"])

    fig = px.bar(
        df,
        x="Outbreak Date",
        y="Flock Size",
        title=title,
        labels={"Outbreak Date": "Outbreak Date", "Outbreak Size": "Outbreak Size"},
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
        yaxis_title="Outbreak Size",
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



def line_graph_maker(df, output_file="outbreak_plot.html", title="Outbreaks Over Time"):
    if df.empty:
        print("No data to plot. Check your date range and filters.")
        return

    df = df.copy()
    df["Outbreak Date"] = pd.to_datetime(df["Outbreak Date"])
    

    fig = px.line(
        df,
        x="Outbreak Date",
        y="Flock Size",
        title=title,
        markers=True,
        labels={"Outbreak Date": "Outbreak Date", "Outbreak Size": "Outbreak Size"},
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
        yaxis_title="Outbreak Size",
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
    
    df = get_time_frame_by_location("2022", "2025")  # full USA
    get_horizontal_comparison(df)
    # df = get_time_frame_by_location("2022", "2025", "Georgia")  # only Georgia
    # get_horizontal_comparison(df, "Georgia")


    if len(frame) > 0:
        unique_states = frame["State"].dropna().unique()
        unique_counties = frame["County"].dropna().unique()

        if len(unique_states) == 1 and len(unique_counties) == 1:
            title_suffix = f"{unique_counties[0]}, {unique_states[0]}"
        elif len(unique_states) == 1:
            title_suffix = unique_states[0]
        else:
            title_suffix = "USA"
    else:
        title_suffix = "Unknown Region"


    title = f"Outbreaks Over Time – {title_suffix}"
    summed_frame = sum_by_date(frame)
    bar_graph_maker(summed_frame, title=title)
    # line_graph_maker(summed_frame)
    
    # TEST: sum in given time frame
    # frame = get_time_frame_by_location("2025-01-13", "2025-01-14")
    # print(sum_by_date(frame))
