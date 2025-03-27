import pandas as pd
import plotly.express as px
# from data_fetcher import get_sorted_dataframe, get_reversed_dataframe
from db_methods import *
from queries import *

df = get_db()
def get_horizontal_comparison(df, *args, show_top_n=None, **kwargs):
    # Step 1: Grab title and output file (if manually set)
    title = kwargs.get("title", None)
    output_file = kwargs.get("output_file", None)

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
    if show_top_n is not None:
        grouped = grouped.head(show_top_n)

    # Step 2: Build dynamic title
    if not title:
        title_parts = []
        if show_top_n is not None:
            plural_label = group_col + "s" if not group_col.endswith("s") else group_col
            title_parts.append(f"Top {show_top_n} {plural_label}")
        title_parts.append(f"Percent of Outbreaks by {group_col} – {scope_name}")
        title = " – ".join(title_parts)


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
        yaxis=dict(
            autorange="reversed",
            tickfont=dict(size=12),
        ),
        height=max(400, 30 * len(grouped))  # ⬅️ Dynamic height based on # of bars
    )


    fig.update_traces(
        texttemplate='%{text:.2f}%',
        textposition='outside'
    )

    # Step 3: Auto-generate output file name if none was provided
    if output_file is None:
        safe_scope = scope_name.lower().replace(" ", "_")
        safe_group = group_col.lower()
        top_tag = f"top{show_top_n}_" if show_top_n is not None else ""
        output_file = f"{top_tag}{safe_group}s_comparison_{safe_scope}.html"

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
    # get_horizontal_comparison(df)
    get_horizontal_comparison(df, show_top_n=10)
    # df = get_time_frame_by_location("2022", "2025", "Georgia")  # only Georgia
    # get_horizontal_comparison(df, "Georgia")
    # get_horizontal_comparison(df, "Georgia", show_top_n=10)
    # get_horizontal_comparison(df, output_file="ga_top10.html", show_top_n=10)
    # get_horizontal_comparison(df, title="Top Counties in GA", output_file="myplot.html", show_top_n=15)



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
