from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

DATA_PATH = Path(__file__).with_name("spacex_launch_dash.csv")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"{DATA_PATH.name} must be stored in the same directory as this script."
    )

spacex_df = pd.read_csv(DATA_PATH)
if "Unnamed: 0" in spacex_df.columns:
    spacex_df = spacex_df.drop(columns="Unnamed: 0")

min_payload = float(spacex_df["Payload Mass (kg)"].min())
max_payload = float(spacex_df["Payload Mass (kg)"].max())
SITE_OPTIONS = ["ALL"] + sorted(spacex_df["Launch Site"].unique().tolist())


def make_success_pie(selected_site):
    if selected_site == "ALL":
        success_by_site = (
            spacex_df.loc[spacex_df["class"].eq(1)]
            .groupby("Launch Site")
            .size()
            .rename("Successful Landings")
            .reset_index()
        )
        return px.pie(
            success_by_site,
            values="Successful Landings",
            names="Launch Site",
            title="Successful Falcon 9 Landings by Launch Site",
            hole=0.25,
        )

    site_df = spacex_df.loc[spacex_df["Launch Site"].eq(selected_site)].copy()
    outcome_counts = (
        site_df["class"]
        .map({0: "Failure / no success", 1: "Success"})
        .value_counts()
        .rename_axis("Outcome")
        .reset_index(name="Missions")
    )
    return px.pie(
        outcome_counts,
        values="Missions",
        names="Outcome",
        title=f"Landing Outcomes — {selected_site}",
        hole=0.25,
    )


def make_payload_scatter(selected_site, payload_range):
    low, high = map(float, payload_range)
    filtered = spacex_df.loc[
        spacex_df["Payload Mass (kg)"].between(low, high, inclusive="both")
    ].copy()

    if selected_site != "ALL":
        filtered = filtered.loc[filtered["Launch Site"].eq(selected_site)]

    scope = "All Sites" if selected_site == "ALL" else selected_site

    if filtered.empty:
        fig = go.Figure()
        fig.add_annotation(
            text="No missions match the selected site and payload range.",
            x=0.5, y=0.5, xref="paper", yref="paper",
            showarrow=False,
        )
        fig.update_layout(
            title=f"Payload Mass vs. Landing Outcome — {scope}",
            xaxis_title="Payload Mass (kg)",
            yaxis_title="Landing outcome",
        )
        return fig

    filtered["Landing Outcome"] = filtered["class"].map(
        {0: "Failure / no success", 1: "Success"}
    )
    fig = px.scatter(
        filtered,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        symbol="Landing Outcome",
        hover_data=[
            "Flight Number", "Launch Site",
            "Booster Version", "Landing Outcome"
        ],
        title=f"Payload Mass vs. Landing Outcome — {scope}",
    )
    fig.update_yaxes(
        tickmode="array",
        tickvals=[0, 1],
        ticktext=["Failure / no success", "Success"],
        range=[-0.15, 1.15],
        title="Landing outcome",
    )
    return fig


app = Dash(__name__)
app.title = "SpaceX Launch Analytics"

app.layout = html.Div(
    [
        html.H1(
            "SpaceX Falcon 9 Launch Analytics Dashboard",
            style={"textAlign": "center", "marginBottom": "6px"},
        ),
        html.P(
            "Explore historical first-stage landing outcomes by launch site "
            "and payload range.",
            style={"textAlign": "center", "marginTop": "0"},
        ),
        html.Div(
            [
                html.Label("Launch site"),
                dcc.Dropdown(
                    id="site-dropdown",
                    options=[
                        {"label": "All Sites", "value": "ALL"},
                        *[
                            {"label": site, "value": site}
                            for site in sorted(spacex_df["Launch Site"].unique())
                        ],
                    ],
                    value="ALL",
                    clearable=False,
                    searchable=True,
                ),
            ],
            style={"maxWidth": "760px", "margin": "20px auto"},
        ),
        dcc.Graph(id="success-pie-chart"),
        html.Div(
            [
                html.Label("Payload range (kg)"),
                dcc.RangeSlider(
                    id="payload-slider",
                    min=0,
                    max=10000,
                    step=500,
                    marks={v: f"{v:,}" for v in range(0, 10001, 2000)},
                    value=[min_payload, max_payload],
                    allowCross=False,
                    tooltip={"placement": "bottom", "always_visible": False},
                ),
            ],
            style={"maxWidth": "900px", "margin": "20px auto 35px auto"},
        ),
        dcc.Graph(id="success-payload-scatter-chart"),
    ],
    style={
        "maxWidth": "1200px",
        "margin": "0 auto",
        "padding": "20px",
        "fontFamily": "Arial, sans-serif",
    },
)


@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value"),
)
def update_pie(selected_site):
    return make_success_pie(selected_site)


@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    Input("site-dropdown", "value"),
    Input("payload-slider", "value"),
)
def update_scatter(selected_site, payload_range):
    return make_payload_scatter(selected_site, payload_range)


if __name__ == "__main__":
    app.run(debug=False)
