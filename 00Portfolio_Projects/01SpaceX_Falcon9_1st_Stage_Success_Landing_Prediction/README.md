# SpaceX Falcon 9 Data Analytics & Machine Learning Portfolio

## Overview

This project is an end-to-end data analytics and machine learning portfolio built around historical SpaceX Falcon 9 launch and first-stage landing data.

It was developed from the IBM Data Science Professional Certificate capstone and then substantially refined into a research-oriented portfolio project. The final workflow demonstrates the full analytics lifecycle:

**API acquisition → web scraping → data wrangling → SQL analysis → exploratory visualization → geospatial analysis → interactive dashboarding → machine learning and model evaluation**

The project is designed to show not only technical implementation, but also analytical reasoning, validation discipline, interpretation, and awareness of methodological limitations.

The repository contains eight numbered notebooks that form one connected workflow, plus supporting datasets, scripts, maps, figures, and a companion research-style report.

---

## Project Objective

The central analytical question is:

> **Can historical Falcon 9 mission characteristics help explain and predict first-stage landing success?**

The project approaches this question by collecting and reconciling launch data from multiple sources, constructing a binary landing-success target, exploring launch-site/orbit/payload/booster/temporal patterns, querying structured mission data with SQL, examining launch-site geography, building an interactive Plotly Dash application, and comparing multiple classification algorithms under stronger validation designs.

---

## End-to-End Workflow

### 01 — API Data Collection

`01Space-X_Data_Collection_API.ipynb`

The first stage collects historical SpaceX launch data through the SpaceX API and enriches launch records with related rocket, payload, launchpad, and core information.

Because the API endpoints used in the original analysis later became unavailable, this notebook preserves the original successful execution and historical outputs rather than replacing them with new external data.

**Skills:** REST APIs, JSON parsing, nested data extraction, entity-level enrichment, reproducibility under source unavailability.

### 02 — Web Scraping

`02Space-X_Webscraping.ipynb`

A second source is collected from an archived Wikipedia page containing Falcon 9 launch records.

The portfolio version improves the original scraping logic with timeout/error handling, schema-based table detection, reusable parsing functions, validation of dates/missingness/duplicates, and archived execution support.

**Skills:** `requests`, `BeautifulSoup`, `pandas.read_html`, HTML parsing, defensive scraping.

### 03 — Data Wrangling and Target Construction

`03Space-X_Data_Wrangling.ipynb`

The raw launch data is cleaned and transformed into an analysis-ready dataset. A major improvement is the construction of the landing-success target from explicit semantic outcome rules rather than positional assumptions.

Final modeling sample:

- **90 missions**
- **60 successful landings**
- **30 failures / no-success outcomes**
- **66.7% overall success rate**

**Skills:** cleaning, missing-value auditing, categorical normalization, target engineering, validation, reproducible export.

### 04 — SQL Exploratory Analysis

`04Space-X_EDA_SQL_Sqllite.ipynb`

This stage preserves the original SQL workflow:

**CSV → pandas → SQLite staging table → cleaned SQL analysis table → exploratory queries**

Selected findings:

- four historical launch-site labels;
- NASA CRS total payload mass: **45,596 kg**;
- Falcon 9 v1.1 average payload: **2,534.67 kg**;
- first successful ground landing: **2015-12-22**;
- maximum payload: **15,600 kg**;
- mission outcome distribution in the SQL dataset: **100 successes vs. 1 failure**.

**Skills:** SQLite, SQL aggregation, filtering, grouping, staging, query validation.

### 05 — Exploratory Data Analysis and Feature Engineering

`05Space-X_EDA_Data_Visualization.ipynb`

This notebook explores landing success by flight number, payload mass, launch site, orbit, launch year, and operational characteristics, then creates the one-hot encoded feature matrix used for machine learning.

Selected results from the 90-mission modeling dataset:

| Launch Site | Observed Success Rate |
|---|---:|
| KSC LC 39A | 77.3% |
| VAFB SLC 4E | 76.9% |
| CCAFS SLC 40 | 60.0% |

Payload success rates are non-linear:

| Payload Band | Success Rate |
|---|---:|
| 0–2,000 kg | 58.3% |
| 2,000–4,000 kg | 69.2% |
| 4,000–6,000 kg | 52.9% |
| 6,000–8,000 kg | 50.0% |
| 8,000+ kg | 87.0% |

Yearly success improved strongly but not monotonically:

- 2010–2013: 0%
- 2014–2015: 33.3%
- 2016: 62.5%
- 2017: 83.3%
- 2018: 61.1%
- 2019: 90.0%
- 2020: 84.2%

**Skills:** EDA, visualization, grouping, categorical encoding, feature engineering, temporal interpretation.

### 06 — Geospatial Analysis with Folium

`06Space-X_Folium_Visualization_Launch_Site_Location.ipynb`

The geospatial stage uses Folium to map launch sites, landing outcomes, and proximity references. The final portfolio version uses an **Esri World Street Map** basemap for deeper street-level context.

The 56-record geospatial snapshot gives these observed site rates:

| Launch Site | Success Rate |
|---|---:|
| KSC LC-39A | 76.9% |
| CCAFS SLC-40 | 42.9% |
| VAFB SLC-4E | 40.0% |
| CCAFS LC-40 | 26.9% |

CCAFS LC-40 proximity case study:

- selected coastline reference: approximately **0.58 km**
- selected nearby city reference: approximately **23.16 km**

These are descriptive reference distances, not GIS nearest-neighbor estimates.

**Skills:** Folium, marker clusters, coordinates, interactive mapping, haversine distance, spatial interpretation.

### 07 — Interactive Plotly Dash Dashboard

`07SpaceX_Dashboard_DashApp.ipynb`

The dashboard allows users to select launch sites, filter payload ranges, compare success/failure composition, and explore payload mass versus landing outcome by booster category.

The portfolio refactor also corrects the original all-sites pie chart so that it actually counts successful landing records.

Audited findings from the 56-row dashboard dataset:

- KSC LC-39A has the most successful landings: **10**
- KSC LC-39A has the highest observed site rate: **76.9%**
- 2,000–4,000 kg has the highest fixed 2,000 kg payload-band rate: **61.9%**
- 6,000–8,000 kg has the lowest fixed-band rate: **0%**
- `B5` is nominally 100% but has only one observation
- among multi-observation booster categories, `FT` is highest at **66.7%**

**Skills:** Plotly, Dash, callbacks, interactive filtering, reusable chart functions, dashboard validation.

### 08 — Machine Learning Classification

`08SpaceX_Machine_Learning_Prediction_Classification.ipynb`

This is the most important analytical stage.

The original IBM notebook compared Logistic Regression, SVM, Decision Tree, and KNN on a single 18-observation test set, where all four reported **83.33% accuracy**.

The portfolio version strengthens the evaluation with leakage-safe pipelines, a majority-class baseline, repeated nested stratified cross-validation, multiple metrics, temporal holdout testing, and interpretable feature analysis.

#### Repeated nested cross-validation

| Model | Accuracy | Balanced Accuracy | Failure Recall | Success Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Decision Tree | 0.829 | **0.800** | **0.713** | 0.887 | 0.873 | 0.846 |
| SVM | **0.838** | 0.792 | 0.653 | **0.930** | **0.884** | **0.878** |
| Logistic Regression | 0.807 | 0.767 | 0.647 | 0.887 | 0.858 | 0.864 |
| KNN | 0.800 | 0.737 | 0.547 | 0.927 | 0.861 | 0.834 |

Interpretation:

- **SVM** provides the strongest average overall discrimination.
- **Decision Tree** provides the strongest balanced accuracy and failure detection.
- Differences are meaningful but not large enough to justify claiming a decisive single winner.

#### Temporal holdout

Latest 18 missions:

- **15 successes**
- **3 failures**
- period: **2020-01-19 to 2020-11-05**

| Model | Accuracy | Balanced Accuracy | Failure Recall | Success Recall |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.889 | 0.667 | 0.333 | 1.000 |
| SVM | 0.889 | 0.667 | 0.333 | 1.000 |
| Decision Tree | 0.889 | 0.667 | 0.333 | 1.000 |
| KNN | 0.833 | 0.500 | 0.000 | 1.000 |
| Majority Baseline | 0.833 | 0.500 | 0.000 | 1.000 |

The key lesson is that **high accuracy can be misleading when later missions are heavily success-dominated**. The three strongest temporal models classify all 15 successes correctly but detect only **1 of 3 failures**.

**Skills:** classification, `GridSearchCV`, nested CV, class-imbalance analysis, ROC-AUC, balanced accuracy, confusion matrices, temporal validation, model interpretation, leakage control.

---

## Research Contribution of the Portfolio Version

The main contribution of this portfolio is methodological.

It shows how a course-based analytics workflow can be upgraded into a more rigorous research-style project by:

- validating each analytical stage;
- preserving provenance across different historical data snapshots;
- correcting fragile or misleading code;
- maintaining reproducibility when live sources disappear;
- separating descriptive findings from causal claims;
- using stronger model-validation strategies;
- evaluating both success and failure detection;
- testing chronological generalization;
- interpreting uncertainty instead of optimizing for a headline accuracy number.

---

## Recommended Repository Structure

```text
SpaceX_Falcon9_Analytics/
│
├── 01_Data_Collection_API/
├── 02_Web_Scraping/
├── 03_Data_Wrangling/
├── 04_SQL_EDA/
├── 05_EDA_Visualization/
├── 06_Geospatial/
├── 07_Dashboard/
├── 08_Machine_Learning/
├── report/
└── README.md
```

Keep the numbered notebook sequence intact because the analytical stages build on one another.

---

## Technologies Used

- Python
- pandas
- NumPy
- requests
- BeautifulSoup
- SQLite / SQL
- matplotlib
- seaborn
- Plotly
- Dash
- Folium
- scikit-learn
- Jupyter Notebook

---

## How to Run

Install the main dependencies:

```bash
pip install pandas numpy requests beautifulsoup4 lxml matplotlib seaborn plotly dash folium scikit-learn jupyter
```

Launch Jupyter:

```bash
jupyter notebook
```

Run the notebooks in order:

```text
01 → 02 → 03 → 04 → 05 → 06 → 07 → 08
```

### Reproducibility note

Notebook 01 preserves a historical successful SpaceX API execution. The API endpoints used during the original project later became unavailable, so API-dependent cells may not reproduce if rerun today.

The repository therefore retains the historical response/output artifacts used by the remaining notebooks.

For the standalone Dash application, keep `spacex_launch_dash.csv` in the same directory as the app script and run:

```bash
python spacex_dash-app.py
```

---

## Key Analytical Takeaways

1. Falcon 9 landing success improved substantially over the historical period, although not monotonically.
2. Launch site, booster generation, reuse history, recovery configuration, orbit, and payload are associated with landing outcomes.
3. Payload mass does not have a simple monotonic relationship with landing success.
4. KSC LC-39A consistently shows strong observed performance in the relevant historical snapshots.
5. Later booster generations generally outperform earlier ones, although booster generation is also related to mission era.
6. Machine-learning models outperform a naïve majority baseline under repeated validation.
7. SVM provides the strongest average overall discrimination, while Decision Tree performs best on balanced accuracy and failure recall.
8. Temporal validation shows that strong headline accuracy can conceal weak failure detection.

---

## Limitations

Important limitations include:

- different stages of the original IBM project use different historical snapshots;
- the main modeling dataset contains only 90 observations;
- landing success becomes strongly imbalanced toward success in later years;
- the feature matrix is high-dimensional relative to sample size;
- several operational variables are correlated with mission era and program maturity;
- predictive importance should not be interpreted as causal importance;
- historical results should not automatically be generalized to later SpaceX operations.

---

## Companion Research Report

A full research-style companion report is included with the project:

**SpaceX Falcon 9 Data Analytics & Machine Learning: An End-to-End Applied Analytics Portfolio**

The report integrates the eight notebooks into a single research narrative covering motivation, data provenance, methodology, empirical findings, model evaluation, limitations, and relevance to business/data analytics.

---

## Business Analytics Relevance

Although the application domain is aerospace, the methods demonstrated here transfer directly to business analytics problems involving:

- operational risk;
- performance prediction;
- asset reuse;
- process improvement;
- location analysis;
- KPI dashboards;
- model selection;
- imbalanced classification;
- longitudinal performance change;
- evidence-based decision support.

The project demonstrates how data can move from **acquisition and cleaning to descriptive analysis, interactive communication, predictive modeling, and decision support**.

---

## Author

**Keman Xiang**

Portfolio project prepared as part of a broader application portfolio in business analytics and data science.

---

## Acknowledgment

This project builds on the SpaceX capstone from the **IBM Data Science Professional Certificate**.

The original analytical structure and educational datasets provided the foundation. The portfolio version substantially refactors, validates, extends, and interprets the workflow for research-oriented presentation.

---

## License

This repository is intended for educational and portfolio use. Verify the licensing terms of third-party datasets, course materials, and external map providers before redistribution.
