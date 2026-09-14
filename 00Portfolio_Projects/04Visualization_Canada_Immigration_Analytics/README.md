# Canada Immigration Visual Analytics with Python

A visualization-centered data analytics portfolio project examining
international immigration flows to Canada from **1980 to 2013** using
**Pandas, Matplotlib, Seaborn, and Folium**.

Rather than treating visualization as a final presentation step, this
project uses visual analysis as the primary analytical method: preparing
a reproducible dataset, investigating temporal and cross-sectional
patterns, comparing distributions and composition, examining
concentration and variability, and mapping the geographic structure of
immigration origins.

The project was developed as part of a **Business Analytics / Data
Analytics portfolio** and is designed to demonstrate Python-based
exploratory analysis, statistical visualization, geospatial
visualization, data preparation, and analytical communication.

------------------------------------------------------------------------

## Project Overview

The analysis is based on the United Nations dataset ***International
Migration Flows to and from Selected Countries: The 2015 Revision***.
The Canada workbook reports annual immigration flows by
citizenship/origin and includes geographic classifications such as
continent, region, and development group.

The final analytical dataset covers:

-   **1980--2013**
-   **34 annual observations**
-   **194 identified international origins**
-   Country/origin, continent, region, and development-group dimensions
-   Annual immigration counts and cumulative immigration totals

The raw workbook also contains special records such as `Canada`,
`Unknown`, and `Total`. These are handled explicitly during
preprocessing rather than being silently removed.

> **Interpretation:** `Country` is used as a convenient analytical
> label, but the underlying UN source is classified by
> citizenship/origin. The observations represent **immigration flows**,
> not Canada's resident immigrant stock.

------------------------------------------------------------------------

## Analytical Questions

The project is question-driven rather than organized as a catalog of
plotting functions. It investigates questions including:

1.  How did total identified international immigration to Canada change
    over time?
2.  Which origin countries contributed the largest cumulative flows?
3.  How did the trajectories of major source countries differ?
4.  How did the continental composition of immigration change?
5.  How unevenly were immigration flows distributed across origins?
6.  How concentrated were cumulative flows among the largest source
    countries?
7.  Which major origins exhibited the greatest temporal variability?
8.  How do country-level distributions differ across continents and
    development groups?
9.  What patterns become visible after normalizing country trajectories?
10. How did the global geography of immigration origins change between
    1980 and 2013?

------------------------------------------------------------------------

## Project Workflow

``` text
Canada.xlsx
    │
    ▼
01 Data Preparation
    │
    ├── scope definition
    ├── cleaning and validation
    ├── geographic classifications
    └── analysis-ready CSV/XLSX
    │
    ▼
02 Exploratory Visual Analytics
    │
    ├── temporal trends
    ├── rankings and country trajectories
    ├── continental composition
    ├── distributions
    ├── concentration
    └── variability
    │
    ▼
03 Advanced Statistical Visualization
    │
    ├── boxplots and violin plots
    ├── normalized composition
    ├── standardized heatmaps
    ├── descriptive trend visualization
    └── correlation structure
    │
    ▼
04 Geospatial Visualization
    │
    ├── geographic linkage audit
    ├── cumulative choropleth
    ├── 2013 choropleth
    └── change in immigration share
```

------------------------------------------------------------------------

## Notebooks

### `01_Data_Preparation_Canada_Immigration.ipynb`

Builds the reproducible analytical foundation of the project.

Key tasks include:

-   reading the original `Canada.xlsx` workbook;
-   documenting source metadata and workbook structure;
-   defining the international-origin analytical scope;
-   explicitly excluding aggregate/non-geographic records;
-   standardizing country, continent, region, and development-group
    fields;
-   validating uniqueness, completeness, numeric values, and
    non-negative counts;
-   calculating cumulative immigration from 1980--2013;
-   exporting a single cleaned dataset for all downstream notebooks.

This notebook separates **data preparation** from **visual analysis**,
preventing preprocessing logic from being repeated throughout the
project.

### `02_Exploratory_Visual_Analytics_Canada_Immigration.ipynb`

The main exploratory analysis notebook. It consolidates the useful
material from the original line, area, histogram, bar, box, scatter,
bubble, and direct-Matplotlib exercises into one analytical workflow.

Major visual analyses include:

-   total immigration through time;
-   top 15 immigration origins;
-   annual trajectories of the five largest origins;
-   continental composition through time;
-   distribution of country-level immigration in 2013;
-   cumulative concentration of immigration by origin;
-   average annual immigration versus temporal variability;
-   an annotated Haiti case around the 2010 earthquake period.

Pandas is used primarily for transformation and aggregation, while
Matplotlib provides direct control over the final visualizations.

### `03_Advanced_Statistical_Visualization_Canada_Immigration.ipynb`

Extends the EDA with statistical graphics that reveal structure not
easily visible in conventional charts.

Analyses include:

-   boxplots of country-level totals by continent;
-   violin plots comparing developed and developing regions;
-   normalized continental-share heatmaps;
-   within-country z-score heatmaps for major origins;
-   a descriptive linear trend visualization;
-   correlation heatmaps for continental immigration series.

The fitted regression line is used only as a **descriptive visual
summary**, not as a forecasting or causal model.

WordCloud and repeated Waffle-chart exercises from the original
instructional material were intentionally removed because they added
less analytical precision than the retained visualizations.

### `04_Geospatial_Visualization_Canada_Immigration.ipynb`

Concludes the project with interactive geospatial analysis using Folium.

The notebook:

-   harmonizes UN origin labels with world geographic boundaries;
-   audits mapped and unmapped origins before visualization;
-   creates a cumulative 1980--2013 immigration choropleth;
-   maps the geographic pattern specifically for 2013;
-   maps changes in each country's share of Canadian immigration between
    1980 and 2013;
-   exports the Folium maps as standalone interactive HTML files.

This stage demonstrates that geographic linkage itself is part of the
analytical workflow rather than an invisible preprocessing step.

------------------------------------------------------------------------

## Selected Findings

The visual analysis identifies several broad patterns:

-   Canadian immigration increased over the long run, but the annual
    series contains substantial peaks, declines, and recoveries rather
    than a single smooth growth path.
-   **India and China** were the two largest cumulative origins in the
    prepared dataset, followed by the **United Kingdom** and the
    **Philippines**.
-   Major source countries followed different temporal trajectories;
    cumulative importance does not imply a common historical pattern.
-   The geographic composition shifted materially toward **Asia**, while
    Europe's relative contribution declined over the observation period.
-   Country-level immigration flows were strongly right-skewed: many
    origins contributed modest counts while a relatively small number
    contributed very large flows.
-   Cumulative immigration was concentrated among a minority of origins.
-   Statistical graphics show substantial heterogeneity within
    continents and overlap between developed- and developing-region
    origin distributions.
-   Standardizing major-country trajectories reveals different periods
    of unusually high and low immigration relative to each country's own
    history.
-   Geospatial analysis confirms that immigration origins were
    geographically clustered and that the spatial structure in **2013**
    differed from the cumulative 1980--2013 pattern.

These findings are **descriptive rather than causal**. The project
identifies patterns and relationships but does not claim to explain the
policy, economic, political, or demographic mechanisms that produced
them.

------------------------------------------------------------------------

## Visualization Strategy

A central design principle of the project is that chart selection should
follow the analytical question.

  -----------------------------------------------------------------------
  Analytical objective                Visualization
  ----------------------------------- -----------------------------------
  Trend through time                  Line chart

  Rank source countries               Horizontal bar chart

  Compare country trajectories        Multi-series line chart

  Show composition through time       Stacked area chart

  Examine cross-country distribution  Histogram / boxplot / violin plot

  Quantify concentration              Cumulative concentration curve

  Compare scale and variability       Scatter / bubble-style chart

  Compare normalized composition      Percentage heatmap

  Compare temporal patterns           Z-score heatmap
  independent of scale                

  Summarize association               Regression / correlation
                                      visualization

  Examine spatial structure           Interactive choropleth
  -----------------------------------------------------------------------

The project intentionally avoids reproducing the same graph through both
Pandas and Matplotlib simply to demonstrate syntax. It also omits chart
types when a more precise visual encoding answers the analytical
question better.

------------------------------------------------------------------------

## Interactive Geospatial Outputs

The Folium notebook exports three standalone browser-based maps:

``` text
maps/
├── canada_immigration_total_1980_2013.html
├── canada_immigration_2013.html
└── canada_immigration_share_change_1980_2013.html
```

Static PNG versions can also be included in the repository and portfolio
report for environments where interactive HTML is not rendered directly.

------------------------------------------------------------------------

## Repository Structure

``` text
Canada_Immigration_Visual_Analytics/
│
├── 01_Data_Preparation_Canada_Immigration.ipynb
├── 02_Exploratory_Visual_Analytics_Canada_Immigration.ipynb
├── 03_Advanced_Statistical_Visualization_Canada_Immigration.ipynb
├── 04_Geospatial_Visualization_Canada_Immigration.ipynb
│
├── data/
│   ├── Canada.xlsx
│   ├── canada_immigration_clean.csv
│   └── world_countries.geojson
│
├── maps/
│   ├── canada_immigration_total_1980_2013.html
│   ├── canada_immigration_2013.html
│   └── canada_immigration_share_change_1980_2013.html
│
├── figures/
│   ├── canada_immigration_total_1980_2013.png
│   ├── canada_immigration_2013.png
│   └── canada_immigration_share_change_1980_2013.png
│
├── Canada_Immigration_Python_Visualization_Portfolio_Report_Rich.docx
└── README.md
```

The exact folder organization can be adjusted without changing the
analytical workflow.

------------------------------------------------------------------------

## Technologies

-   **Python**
-   **Pandas** --- data import, cleaning, transformation, aggregation,
    reshaping
-   **NumPy** --- numerical operations
-   **Matplotlib** --- exploratory and publication-style visualization
-   **Seaborn** --- statistical visualization
-   **Folium** --- interactive geospatial visualization
-   **GeoPandas / GeoJSON** --- geographic boundary preparation and
    linkage
-   **Jupyter Notebook** --- reproducible analytical workflow

------------------------------------------------------------------------

## Reproducibility

The notebooks are intended to run sequentially:

``` text
01 → 02 → 03 → 04
```

Notebook 01 creates the cleaned analytical dataset used by the remaining
notebooks.

A typical environment requires:

``` bash
pip install pandas numpy matplotlib seaborn folium geopandas openpyxl jupyter
```

Then launch Jupyter:

``` bash
jupyter notebook
```

Run Notebook 01 first, followed by Notebooks 02--04.

------------------------------------------------------------------------

## Data Source

The immigration workbook is derived from:

**United Nations, Department of Economic and Social Affairs, Population
Division (2015). *International Migration Flows to and from Selected
Countries: The 2015 Revision*. United Nations database,
POP/DB/MIG/Flow/Rev.2015.**

The project uses the Canada data classified by citizenship/origin for
the period 1980--2013.

The geographic boundary layer used for the final Folium workflow is
based on **Natural Earth low-resolution world boundaries**. Country-name
aliases are handled explicitly in Notebook 04 because geographic
datasets and migration datasets do not always use identical naming
conventions.

------------------------------------------------------------------------

## Methodological Limitations

Several limitations should be considered when interpreting the results:

-   The analysis is descriptive and does not establish causal
    relationships.
-   The source is classified by citizenship/origin and should not be
    interpreted as place of birth or immigrant stock.
-   Aggregating 1980--2013 into a cumulative total can hide substantial
    temporal changes.
-   Development-group and continent classifications simplify
    heterogeneous countries into broad categories.
-   Choropleth maps can visually overemphasize geographically large
    countries.
-   Low-resolution world boundaries do not independently represent every
    microstate, island, or special administrative region in the
    immigration dataset.
-   Correlation and fitted trend visualizations summarize association
    only and should not be interpreted causally.

These limitations are addressed where possible through complementary
visualizations rather than relying on any single chart.

------------------------------------------------------------------------

## Portfolio Relevance

This project is designed to demonstrate a different analytical
capability from portfolio projects centered on regression or machine
learning.

Its emphasis is **visual analytics**: transforming raw data into
interpretable evidence and selecting visual encodings that match the
analytical problem.

The project demonstrates:

-   reproducible data preparation;
-   exploratory data analysis;
-   visual comparison and statistical reasoning;
-   temporal and distributional analysis;
-   multivariate visualization;
-   geospatial data integration;
-   interactive mapping;
-   critical visualization selection;
-   interpretation of analytical limitations;
-   communication of results for non-technical and technical audiences.

These capabilities are directly relevant to **Business Analytics and
Data Analytics**, where effective analysis requires not only computation
but also the ability to identify patterns, evaluate evidence, and
communicate complex information clearly for research and
decision-making.

------------------------------------------------------------------------

## Companion Report

A research-style companion report is included in the repository:

**`Canada_Immigration_Python_Visualization_Portfolio_Report_Rich.docx`**

The report presents the motivation, methodology, empirical findings,
visualization rationale, limitations, and relevance to business/data
analytics without duplicating the notebooks cell by cell. It also
incorporates the major exploratory, statistical, and geospatial
visualizations as a standalone portfolio document.

------------------------------------------------------------------------

## Project Positioning

**Primary focus:** Python Visualization & Exploratory Visual Analytics

**Methods:** Data Preparation · EDA · Statistical Visualization ·
Geospatial Visualization · Visual Communication

**Libraries:** Pandas · Matplotlib · Seaborn · Folium · GeoPandas

This project is part of a broader analytics portfolio and is
intentionally focused on **visual analytical reasoning rather than
predictive modeling**.
