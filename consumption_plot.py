import pandas as pd
import plotly.graph_objects as go
import base64
from IPython.display import display, HTML
from pathlib import Path

def create_consumption_plot():
    # Get path to data file (in data/ folder)
    data_path = Path.cwd() / "data" / "consumption_data.csv"
    
    df = pd.read_csv(data_path).set_index('Year').transpose()
    df.index = pd.to_datetime(df.index, format="%Y", errors="coerce")
    df = df.dropna(how='all')
    df = df.sort_index()

    default_column = "Consumption (GWh)  ̶  based on estimated sales"
    y_axis_options = df.columns.tolist()

    # Create the figure
    fig = go.Figure()

    for y_col in y_axis_options:
        fig.add_trace(
            go.Scatter(x=df.index, y=df[y_col], name=y_col, visible=(y_col == default_column))
        )

    # Create buttons for dropdown
    buttons = []
    for y_col in y_axis_options:
        buttons.append(
            dict(
                label=y_col,
                method="update",
                args=[{"visible": [col == y_col for col in y_axis_options]}, {}]
            )
        )

    fig.update_layout(
        updatemenus=[
            dict(
                active=y_axis_options.index(default_column),
                buttons=buttons,
                direction="down",
                showactive=True,
                x=1.05,
                xanchor="left",
                y=0.5,
                yanchor="middle"
            )
        ],
        xaxis_title="Year",
        yaxis_title="GWh",
        margin=dict(b=100)  # Extra bottom margin for the download button
    )

    # Prepare download button HTML
    csv_string = df.to_csv().encode()
    b64 = base64.b64encode(csv_string).decode()
    download_html = f"""
    <div style="margin: 20px; text-align: left;">
        <a href="data:file/csv;base64,{b64}" 
           download="consumption_data.csv"
           style="padding: 10px 20px; 
                  background-color: #0074D9; 
                  color: white; 
                  text-decoration: none;
                  border-radius: 5px;
                  font-family: Arial, sans-serif;">
            Download Consumption Data (CSV)
        </a>
    </div>
    """

    # Create a wrapper function that will show both
    def show_plot_with_download():
        display(fig)
        display(HTML(download_html))

    # Return both the figure and the display function
    return fig, show_plot_with_download