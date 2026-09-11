# Automobile Pricing Analytics

## A Python-Based Regression Analysis of Vehicle Characteristics and Price

This project presents an end-to-end **Python data analytics and
regression workflow** using the UCI Automobile dataset. It examines how
observable vehicle characteristics are associated with automobile price
and evaluates whether increasingly flexible regression specifications
improve out-of-sample performance.

The project was developed as an independent portfolio study in
**business analytics / data analytics**. Its emphasis is not simply on
fitting predictive models, but on demonstrating a disciplined analytical
process:

**Data Importing & Understanding → Data Cleaning & Feature Engineering →
Exploratory Data Analysis → Regression Model Development → Model
Evaluation & Selection**

A companion research-style report integrates the empirical findings,
methodology, interpretation, limitations, and business relevance without
duplicating the notebooks cell by cell.

------------------------------------------------------------------------

## Project Objectives

The analysis addresses five questions:

1.  How is automobile price distributed in the analytical sample?
2.  Which vehicle characteristics show the strongest empirical
    relationships with price?
3.  How well do simple linear, multiple linear, and polynomial
    regression specifications represent automobile prices?
4.  Does increasing polynomial complexity improve generalization, or
    eventually lead to overfitting?
5.  Which regression specification provides the strongest balance of
    predictive performance, stability, interpretability, and parsimony?

------------------------------------------------------------------------

## Dataset

The project uses the **Automobile dataset** from the UCI Machine
Learning Repository, originally derived from the **1985 Ward's
Automotive Yearbook**.

-   Raw observations: **205**
-   Raw columns in the working dataset: **26**
-   Cleaned analytical observations: **201**
-   Cleaned columns after feature preparation: **29**
-   Exact duplicate rows: **0**
-   Missing price observations removed: **4**

### Data Sources

-   UCI Machine Learning Repository:
    https://archive.ics.uci.edu/dataset/10/automobile
-   Dataset DOI: https://doi.org/10.24432/C5B01C
-   IBM Skills Network-hosted CSV used in the project:
    https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv

> **Important:** This is a small historical automobile dataset. The
> results should not be interpreted as a contemporary vehicle-pricing
> model.

------------------------------------------------------------------------

## Repository Workflow

### 01 --- Data Importing & Initial Understanding

The first notebook establishes the analytical foundation by importing
the raw dataset, assigning and validating the schema, inspecting
dimensions and data types, identifying `?` missing-value markers,
examining missingness by variable, checking duplicate observations, and
documenting the data-quality issues that require treatment.

This stage deliberately separates **data understanding** from later
cleaning decisions.

### 02 --- Data Cleaning & Feature Engineering

The second notebook transforms the raw data into an analysis-ready
table. Key steps include:

-   converting `?` markers to standard missing values;
-   converting numerical variables to appropriate numeric types;
-   mean-imputing selected numerical predictors;
-   replacing missing `num-of-doors` values using the modal category;
-   removing observations without an observed target price;
-   creating supplementary fuel-consumption measures in L/100 km;
-   creating horsepower categories for descriptive analysis; and
-   exporting `auto_cleaned.csv`.

The final cleaned sample contains **201 observations with no remaining
missing values**. Price is deliberately **not imputed**, because it is
the dependent variable used in the regression analysis.

### 03 --- Exploratory Data Analysis

EDA investigates the structure of automobile pricing before model
specification through descriptive statistics, price-distribution
analysis, Pearson correlations and significance tests, scatterplots,
categorical comparisons, boxplots, grouping and pivot analysis, and
examination of overlap among candidate predictors.

#### Selected EDA Findings

  Feature         Pearson correlation with price
  ------------- --------------------------------
  Engine size                          **0.872**
  Curb weight                          **0.834**
  Horsepower                           **0.810**
  Width                                **0.751**
  Highway MPG                         **-0.705**
  Length                               **0.691**
  City MPG                            **-0.687**
  Wheel base                           **0.585**
  Bore                                 **0.543**

The analysis indicates that price is strongly associated with **engine
capacity, vehicle mass, power, physical size, and fuel economy**.
Several of these predictors are also correlated with one another,
motivating multiple regression while requiring caution when interpreting
individual coefficients.

### 04 --- Regression Model Development

The fourth notebook translates the EDA findings into four explicit
regression specifications:

1.  **Simple Linear Regression --- Highway MPG**
2.  **Simple Linear Regression --- Engine Size**
3.  **Multiple Linear Regression --- Horsepower + Curb Weight + Engine
    Size + Highway MPG**
4.  **Polynomial Regression --- Highway MPG**

Model-development performance is examined using R², MSE, RMSE, MAE,
residual diagnostics, and observed-versus-fitted comparisons. These
results are explicitly treated as **in-sample evidence**, not final
measures of predictive performance.

#### In-Sample Model Development Results

  -----------------------------------------------------------------------
  Model                          R²               RMSE                MAE
  -------------- ------------------ ------------------ ------------------
  **Multiple              **0.809**        **\$3,461**        **\$2,451**
  Linear                                               
  Regression ---                                       
  4 Predictors**                                       

  SLR --- Engine              0.761            \$3,872            \$2,794
  Size                                                 

  Polynomial ---              0.674            \$4,523            \$3,201
  Highway MPG                                          
  (Degree 3)                                           

  SLR ---                     0.497            \$5,616            \$3,821
  Highway MPG                                          
  -----------------------------------------------------------------------

### 05 --- Regression Model Evaluation & Selection

The final notebook evaluates whether the developed relationships
generalize beyond the estimation sample.

The evaluation design uses:

-   **80/20 train-test split**;
-   fixed `random_state = 42`;
-   **5-fold cross-validation on the training sample**;
-   training-versus-validation comparison;
-   polynomial complexity analysis; and
-   untouched holdout evaluation.

The holdout test set is not used to select polynomial degree.

#### Polynomial Complexity

Polynomial degrees **1 through 15** are evaluated using training-set
cross-validation. Validation performance improves through **degree 6**,
which achieves the highest mean cross-validation R². At higher degrees,
validation performance eventually deteriorates substantially.

This provides a practical illustration of **overfitting and the
bias-variance trade-off**.

Selected polynomial: **Highway MPG Polynomial Regression --- Degree 6**

------------------------------------------------------------------------

## Final Model Comparison

  --------------------------------------------------------------------------
  Model              Holdout R²   Holdout RMSE    Holdout MAE     Mean CV R²
  -------------- -------------- -------------- -------------- --------------
  **Multiple          **0.764**    **\$5,377**    **\$3,769**      **0.767**
  Linear                                                      
  Regression ---                                              
  4 Predictors**                                              

  SLR --- Engine          0.725        \$5,805        \$3,557          0.718
  Size                                                        

  Polynomial ---          0.546        \$7,453        \$4,486          0.658
  Highway MPG                                                 
  (Degree 6)                                                  

  SLR ---                 0.425        \$8,391        \$5,227          0.444
  Highway MPG                                                 
  --------------------------------------------------------------------------

The **four-predictor Multiple Linear Regression** is the preferred final
specification. It leads both the untouched holdout comparison and the
mean cross-validation comparison.

The result suggests that incorporating information from several
meaningful automobile characteristics provides greater generalizable
value than adding increasingly complex nonlinear structure to highway
MPG alone.

------------------------------------------------------------------------

## Key Analytical Findings

-   **Engine size is the strongest single continuous correlate of
    price** in the analytical sample.
-   Curb weight and horsepower also show strong positive price
    relationships.
-   Fuel economy is negatively associated with price in the bivariate
    analysis.
-   Engine size alone provides a strong SLR benchmark, but a single
    predictor does not capture the full pricing structure.
-   Combining horsepower, curb weight, engine size, and highway MPG
    substantially improves regression performance.
-   Polynomial regression improves the highway-MPG model, but excessive
    polynomial complexity eventually damages validation performance.
-   The final MLR generalizes better than both the single-predictor
    regressions and the selected nonlinear highway-MPG model.

These results support a **multidimensional interpretation of automobile
pricing**: price differences in this historical sample are associated
with multiple dimensions of vehicle power, capacity, physical size,
weight, and efficiency.

------------------------------------------------------------------------

## Analytical Interpretation

One useful result is the difference between **bivariate** and
**multivariate** relationships.

Highway MPG has a strong negative Pearson correlation with price.
However, its coefficient changes when horsepower, curb weight, and
engine size are included simultaneously in the MLR.

This illustrates an important analytical principle:

> A pairwise correlation does not necessarily represent a variable's
> independent relationship with an outcome when correlated predictors
> are considered jointly.

Regression coefficients in this project are therefore interpreted as
**conditional associations**, not causal effects.

------------------------------------------------------------------------

## Methods and Python Skills Demonstrated

### Data Management

`pandas`, `numpy`, schema inspection, missing-value diagnosis, data-type
conversion, variable-specific imputation, filtering, feature
engineering, and cleaned-dataset export.

### Exploratory Data Analysis

Descriptive statistics, distribution analysis, Pearson correlation,
statistical significance testing, grouping and aggregation, pivot
tables, and predictor-overlap analysis.

### Data Visualization

`matplotlib`, scatterplots, regression visualizations, histograms,
boxplots, residual plots, observed-versus-predicted plots, and
model-complexity curves.

### Regression Analysis

Simple Linear Regression, Multiple Linear Regression, Polynomial
Regression, coefficient interpretation, residual diagnostics, R², MSE,
RMSE, and MAE.

### Model Evaluation

Train/test splitting, K-fold cross-validation,
training-versus-validation comparison, polynomial complexity analysis,
overfitting diagnosis, holdout evaluation, model comparison, and
parsimony-based model selection.

------------------------------------------------------------------------

## Project Structure

``` text
automobile-pricing-analytics/
│
├── 01_...Data_Importing...ipynb
├── 02_...Data_Cleaning...ipynb
├── 03_...Exploratory_Data_Analysis...ipynb
├── 04_Regression_Model_Development_Automobile_Pricing.ipynb
├── 05_Regression_Model_Evaluation_Selection_Automobile_Pricing_FINAL.ipynb
│
├── auto.csv
├── auto_cleaned.csv
│
├── Automobile_Pricing_Analytics_Portfolio_Report.docx
└── README.md
```

The notebook numbering indicates the intended execution and analytical
sequence.

------------------------------------------------------------------------

## Research-Style Companion Report

The repository also includes
**`Automobile_Pricing_Analytics_Portfolio_Report.docx`**.

The report presents the project as an integrated empirical study rather
than repeating notebook cells. It covers the analytical motivation,
research questions, dataset provenance, methodology, data preparation,
empirical findings, regression development, polynomial complexity and
overfitting, final model selection, business/data analytics relevance,
limitations, and research extensions.

The notebooks serve as the **reproducible analytical evidence**, while
the report provides the **research-style interpretation and
communication**.

------------------------------------------------------------------------

## Limitations

1.  **Historical dataset** --- the observations originate from the 1985
    Ward's Automotive Yearbook and do not represent the contemporary
    automobile market.
2.  **Small sample size** --- only 201 observations remain after
    removing vehicles without observed prices.
3.  **Missing-data treatment** --- mean imputation preserves
    observations but may reduce natural variability.
4.  **Observational data** --- the analysis supports association, not
    causal inference.
5.  **Multicollinearity** --- several vehicle characteristics contain
    overlapping information.
6.  **Specification scope** --- the final MLR intentionally uses a
    compact group of continuous technical characteristics rather than
    all possible product attributes.
7.  **Price skewness** --- expensive observations can exert substantial
    influence on squared-error metrics.

Potential extensions include alternative missing-data strategies,
categorical controls, formal multicollinearity diagnostics, log-price
specifications, robust regression diagnostics, and validation using a
larger contemporary automobile dataset.

------------------------------------------------------------------------

## Why This Project Matters for Business Analytics

The analytical workflow reflects a common business research problem:

> **How can heterogeneous product attributes be transformed into
> defensible quantitative evidence about price differences?**

The project demonstrates the ability to audit raw external data, make
transparent data-quality decisions, use EDA to motivate modeling,
distinguish correlation from conditional regression relationships,
compare interpretable statistical models, identify overfitting through
validation rather than training fit, preserve an untouched test sample
for final evaluation, and translate technical results into
business-relevant conclusions.

These capabilities are applicable to **pricing analytics, product
analytics, market research, demand analysis, risk analytics, and
empirical business research**.

------------------------------------------------------------------------

## Reproducibility

1.  Obtain `auto.csv` from the source listed above.
2.  Run the notebooks sequentially from **01 through 05**.
3.  Notebook 02 generates the cleaned analytical dataset used by
    subsequent notebooks.
4.  Execute Notebooks 03--05 using the cleaned dataset.
5.  Compare the generated results with the research-style companion
    report.

------------------------------------------------------------------------

## Tools and Libraries

-   Python
-   Jupyter Notebook
-   Pandas
-   NumPy
-   SciPy
-   Matplotlib
-   scikit-learn

------------------------------------------------------------------------

## Citation

> Schlimmer, J. (1985). *Automobile* [Dataset](#dataset). UCI Machine
> Learning Repository. https://doi.org/10.24432/C5B01C

UCI dataset page: https://archive.ics.uci.edu/dataset/10/automobile

------------------------------------------------------------------------

## Author's Note

This project was developed as a portfolio study in **business analytics
and data analytics**, with emphasis on reproducible Python analysis,
statistical reasoning, regression modeling, and research-style
communication.

The objective is not to present the most complex possible predictive
algorithm. Instead, the project emphasizes a transparent progression
from **data quality → empirical evidence → model specification →
validation → interpretation**, demonstrating how Python-based analytics
can support rigorous business research.
