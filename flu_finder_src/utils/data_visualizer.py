import pandas as pd
import plotly.express as px
from db_methods import *
from queries import *

df = get_db()

def get_horizontal_comparison_frequencies(df, *args, show_top_n=None, **kwargs):
    # Step 1: Grab title and output file (if manually set)
    title = kwargs.get("title", None)
    # Replaced "None" with simpler title
    output_file = kwargs.get("output_file", "frequency_comparison_output.html")
    
    if df.empty:
        print("No data to visualize.")
        return

    df = df.copy()

    if len(args) == 0:
        # National level: group by state
        group_col = "State"
        group_col_plural = "States"
        scope_name = "USA"
    elif len(args) == 1:
        # State level: group by county
        group_col = "County"
        group_col_plural = "Counties"
        scope_name = args[0].title()
        df = df[df["State"].str.title() == scope_name]
    else:
        raise ValueError("Only 0 or 1 argument allowed (for national or state-level comparison)")

    # Group and calculate percentage (rounded 3 decimal places)
    grouped = df[group_col].value_counts().reset_index()
    grouped.columns = [group_col, "Outbreak Count"]
    grouped["Frequency (%)"] = (grouped["Outbreak Count"] / grouped["Outbreak Count"].sum() * 100).round(3)

    # Sort from highest to lowest and reverse y-axis later for top-to-bottom effect
    grouped = grouped.sort_values(by="Frequency (%)", ascending=False)
    if show_top_n is not None:
        grouped = grouped.head(show_top_n)

    # Step 2: Build dynamic title
    if not title:
        title_parts = []
        if show_top_n is not None:
            plural_label = group_col_plural if not group_col.endswith("s") else group_col
            title_parts.append(f"Top {show_top_n} {plural_label}")
        title_parts.append(f"Frequency of Outbreaks by {group_col} - {scope_name}")
        title = " - ".join(title_parts)


    fig = px.bar(
        grouped,
        x="Frequency (%)",
        y=group_col,
        orientation='h',
        title=title,
        text="Frequency (%)",
        color="Frequency (%)",
        color_continuous_scale="Blugrn"  # Add '_r' to reverse
    )

    fig.update_layout(
        xaxis_title="Frequency of Outbreaks (%)",
        yaxis_title=group_col,
        title_x=0.5,
        template="plotly_white",
        yaxis=dict(
            autorange="reversed",
            tickfont=dict(size=12),
        ),
        height=max(400, 30 * len(grouped))  # Dynamic height based on # of bars
    )


    fig.update_traces(
        texttemplate='%{text:.2f}%',
        textposition='outside'
    )

    # Step 3: Auto-generate output file name if none was provided
    # Note: I replaced "None" with "horizontal_comparison_output.html"
    #   I think it would be better to be consistent with the file name since it'll only be used in frontend integration
    # if output_file is None:
    #     safe_scope = scope_name.lower().replace(" ", "_")
    #     safe_group = group_col.lower()
    #     top_tag = f"top{show_top_n}_" if show_top_n is not None else ""
    #     output_file = f"{top_tag}{safe_group}s_comparison_{safe_scope}.html"

    config = {"displayModeBar": True,
            "scrollZoom": True,
            "modeBarButtonsToRemove": ["autoScale", "select2d", "lasso2d"]}

    # Save to HTML
    fig.write_html(output_file, config=config)
    print(f"Comparison chart saved to {output_file}")


def get_horizontal_comparison_flock_sizes(df, *args, show_top_n=None, **kwargs):
    # Step 1: Grab title and output file (if manually set)
    title = kwargs.get("title", None)
    # Replaced "None" with simpler title
    output_file = kwargs.get("output_file", "percentage_comparison_output.html")

    if df.empty:
        print("No data to visualize.")
        return

    df = df.copy()

    if len(args) == 0:
        # National level: group by state
        group_col = "State"
        group_col_plural = "States"
        scope_name = "USA"
    elif len(args) == 1:
        # State level: group by county
        group_col = "County"
        group_col_plural = "Counties"
        scope_name = args[0].title()
        df = df[df["State"].str.title() == scope_name]
    else:
        raise ValueError("Only 0 or 1 argument allowed (for national or state-level comparison)")

    # Group and calculate percentage
    grouped = df.groupby(group_col, as_index=False)["Flock Size"].sum()
    grouped["Percentage"] = (grouped["Flock Size"] / grouped["Flock Size"].sum() * 100).round(3)

    # Sort from highest to lowest and reverse y-axis later for top-to-bottom effect
    grouped = grouped.sort_values(by="Percentage", ascending=False)
    if show_top_n is not None:
        grouped = grouped.head(show_top_n)

    # Step 2: Build dynamic title
    if not title:
        title_parts = []
        if show_top_n is not None:
            plural_label = group_col_plural if not group_col.endswith("s") else group_col
            title_parts.append(f"Top {show_top_n} {plural_label}")
        title_parts.append(f"Percentage of affected birds by {group_col} - {scope_name}")
        title = " - ".join(title_parts)


    fig = px.bar(
        grouped,
        x="Percentage",
        y=group_col,
        orientation='h',
        title=title,
        text="Percentage",
        color="Percentage",
        color_continuous_scale="Blugrn"  # Add '_r' to reverse
    )

    fig.update_layout(
        xaxis_title="Percentage",
        yaxis_title=group_col,
        title_x=0.5,
        template="plotly_white",
        yaxis=dict(
            autorange="reversed",
            tickfont=dict(size=12),
        ),
        height=max(400, 30 * len(grouped))  # Dynamic height based on # of bars
    )


    fig.update_traces(
        texttemplate='%{text:.2f}%',
        textposition='outside'
    )

    # Step 3: Auto-generate output file name if none was provided
    # Note: I replaced "None" with "horizontal_comparison_output.html"
    #   I think it would be better to be consistent with the file name since it'll only be used in frontend integration
    # if output_file is None:
    #     safe_scope = scope_name.lower().replace(" ", "_")
    #     safe_group = group_col.lower()
    #     top_tag = f"top{show_top_n}_" if show_top_n is not None else ""
    #     output_file = f"{top_tag}{safe_group}s_comparison_{safe_scope}.html"

    config = {"displayModeBar": True,
            "scrollZoom": True,
            "modeBarButtonsToRemove": ["autoScale", "select2d", "lasso2d"]}

    # Save to HTML
    fig.write_html(output_file, config=config)
    print(f"Comparison chart saved to {output_file}")


def bar_graph_maker(df, output_file="outbreak_bar_graph.html", title="Outbreaks Over Time"):
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


import plotly.express as px

def pie_chart_maker(df, *args):
    df = df.copy()

    # Select scope (0 is national)
    if len(args) == 0:
        scope_name = "USA"
    elif len(args) == 1:
        scope_name = args[0].title()
        df = df[df["State"].str.title() == scope_name]
    else:
        raise ValueError("Only 0 or 1 argument allowed (for national or state-level comparison)")

    # Group by Flock Type and calculate percentage
    grouped = df["Flock Type"].value_counts().reset_index()
    grouped.columns = ["Flock Type", "Count"]
    grouped["Flock (%)"] = (grouped["Count"] / grouped["Count"].sum() * 100).round(3)

    # Create pie chart
    fig = px.pie(
        grouped,
        names="Flock Type",
        values="Count",
        title=f"Flock Type Distribution in {scope_name}",
        hover_data=["Flock (%)"],
    )
    fig.update_traces(
        textinfo="none",  # Removes text labels from pie slices
        hovertemplate="%{label}<br>Count: %{value}<br>Percentage: %{customdata[0]}%",  # Custom hover
        customdata=grouped[["Flock (%)"]],  # Pass percentage to hovertemplate
    )

    # Set figure size
    fig.update_layout(
        width=800,
        height=800,
        # showlegend=True
    )
    
    # Scroll wheel zoom and always visible modebar
    config = {"displayModeBar": True}
    
    # Save to HTML
    fig.write_html("pie_chart.html", config=config)
    print(f"Plot saved to pie_chart.html")


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


def title_picker(frame):
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
    return title_suffix



#------------------------------------------- Method Testing -----------------------------------------#
if __name__ == "__main__":
    # frame = get_time_frame_by_location("2022", "2030")                           # <== National
    # frame = get_time_frame_by_location("2025-01-01", "2025-02-01", "Georgia")    # <== State
    # frame = get_time_frame_by_location("2024", "2030", "ioWA", "BUENA VistA")    # <== County
    # title = f"Outbreaks Over Time - {title_picker(frame)}"
    # summed_frame = sum_by_date(frame)
    # bar_graph_maker(summed_frame, title=title)
    # # line_graph_maker(summed_frame)
    
    # df = get_time_frame_by_location("2022", "3000")  # full USA
    # get_horizontal_comparison_frequencies(df)
    # get_horizontal_comparison_frequencies(df, show_top_n=10)
    # get_horizontal_comparison_frequencies(df, "Georgia")
    # get_horizontal_comparison_frequencies(df, "Georgia", show_top_n=10)
    # get_horizontal_comparison_frequencies(df, output_file="ga_top10.html", show_top_n=10)
    # get_horizontal_comparison_frequencies(df, title="Top Counties in GA", output_file="myplot.html", show_top_n=15)
    
    # get_horizontal_comparison_flock_sizes(df)
    get_horizontal_comparison_flock_sizes(df, show_top_n=10)
    # get_horizontal_comparison_flock_sizes(df, "Georgia")
    # get_horizontal_comparison_flock_sizes(df, "Georgia", show_top_n=10)
    # get_horizontal_comparison_flock_sizes(df, output_file="ga_top10.html", show_top_n=10)
    # get_horizontal_comparison_flock_sizes(df, title="Top Counties in GA", output_file="myplot.html", show_top_n=15)
    
    # pie_chart_maker(df)
    # pie_chart_maker(df, "Georgia")
    
    # TEST: sum in given time frame
    # frame = get_time_frame_by_location("2025-01-13", "2025-01-14")
    # print(sum_by_date(frame))
