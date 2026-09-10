# Predicting Daily Rainfall in Melbourne Using Machine Learning

### A Temporal Validation and Model Comparison Study

> **Python Machine Learning Portfolio Project**\
> A research-oriented predictive analytics study examining whether
> meteorological observations available on day *t* can predict rainfall
> on day *t+1* in metropolitan Melbourne under temporally realistic
> out-of-sample evaluation.

## Project Overview

This project develops an earlier rainfall-classification exercise from
the **IBM Machine Learning Certificate** into a more rigorous
machine-learning portfolio study focused on methodological validity,
reproducibility, and interpretation.

Rather than optimizing a model on a randomized train/test split, the
portfolio version asks a harder forecasting question: **can a model
trained on historical observations generalize to a genuinely later
period?**

The analysis uses Melbourne, Melbourne Airport, and Watsonia
observations from the Australian `weatherAUS` dataset and implements
leakage-safe preprocessing, expanding-window temporal cross-validation,
model comparison, imbalanced-class evaluation, validation-only threshold
selection, probability calibration, permutation importance, and subgroup
robustness diagnostics.

The purpose of the project is not simply to report a high accuracy
score. It demonstrates how validation design, class imbalance, decision
thresholds, temporal change, and heterogeneous errors affect the
interpretation of predictive performance.

## Research Question

**How effectively can meteorological observations available on day *t*
predict rainfall on day *t+1* in the Melbourne metropolitan area, and
how do alternative machine-learning classifiers perform under temporally
realistic out-of-sample evaluation?**

## Key Results

  Result                                        Final 2017 Test
  ------------------------------- -----------------------------
  Selected model                    Histogram Gradient Boosting
  Test observations                                         526
  Rainfall prevalence                                     18.6%
  Accuracy                                            **85.7%**
  Balanced Accuracy                                   **0.676**
  Rainfall Precision                                  **0.717**
  Rainfall Recall                                     **0.388**
  Rainfall F1                                         **0.503**
  ROC-AUC                                             **0.841**
  Average Precision                                   **0.611**
  Brier Score                                         **0.109**
  Validation-selected threshold                       **0.438**

The selected model retained strong ranking ability on the untouched 2017
period, with **ROC-AUC = 0.841** and **Average Precision = 0.611**.
However, rainfall recall declined from **58.7% in 2016 validation to
38.8% in 2017**. This deterioration is an important result: it
demonstrates why a single accuracy statistic can obscure temporal
instability in minority-event detection.

## Analytical Workflow

1.  **Data audit and scope definition** --- examine missingness, class
    imbalance, temporal coverage, seasonality, and station-level
    rainfall patterns.
2.  **Feature engineering** --- preserve the explicit day *t* → day
    *t+1* forecasting horizon and add cyclical calendar features.
3.  **Leakage-safe preprocessing** --- numerical median imputation and
    standardization; categorical mode imputation and one-hot encoding
    inside a `Pipeline`.
4.  **Temporal validation** --- use observations before 2016 for
    development, 2016 for validation, and 2017 as an untouched final
    test.
5.  **Expanding-window tuning** --- select hyperparameters using
    year-based forward validation rather than randomized K-fold
    cross-validation.
6.  **Model comparison** --- benchmark Logistic Regression, Random
    Forest, and Histogram Gradient Boosting against a naïve prior
    classifier.
7.  **Imbalanced-class evaluation** --- report balanced accuracy,
    rainfall precision/recall/F1, ROC-AUC, Average Precision, and Brier
    score in addition to accuracy.
8.  **Decision-threshold analysis** --- choose the classification
    threshold using validation data only.
9.  **Interpretability and robustness** --- examine probability
    calibration, held-out permutation importance, station/season errors,
    and station-holdout generalization.

## Model Comparison

On the 2016 validation period:

  -------------------------------------------------------------------------------
  Model          Accuracy   Balanced       Rain    Rain F1    ROC-AUC     Average
                            Accuracy     Recall                         Precision
  ------------ ---------- ---------- ---------- ---------- ---------- -----------
  Histogram         0.816      0.746      0.587      0.640      0.861   **0.728**
  Gradient                                                            
  Boosting                                                            

  Random            0.819      0.740      0.561      0.633      0.860       0.718
  Forest                                                              

  Logistic          0.802      0.742      0.605      0.631      0.842       0.689
  Regression                                                          
  -------------------------------------------------------------------------------

**Histogram Gradient Boosting** was selected using validation Average
Precision. The differences among the candidate models are relatively
modest; the principal contribution of the project is therefore the
**evaluation design**, not a claim that one algorithm overwhelmingly
dominates the others.

## Why Temporal Validation Matters

The original IBM certificate exercise used a randomized stratified
split. That workflow was useful for learning classification pipelines,
but random splitting is less appropriate for a forecasting claim because
observations from later dates can influence model development for
earlier test observations.

The portfolio redevelopment uses chronological partitions:

-   **Development:** observations before 2016
-   **Validation:** 2016
-   **Final test:** 2017

Hyperparameter tuning uses expanding-year folds so that every validation
period occurs strictly after its corresponding training observations.

This design more closely approximates the real question faced by a
deployed predictive system: **how well does a model trained on the past
perform on the future?**

## Feature Importance

Held-out permutation importance identified the following variables as
the strongest contributors to final-test Average Precision:

  Feature           Mean Permutation Importance
  --------------- -----------------------------
  Pressure3pm                            0.1487
  Humidity3pm                            0.1111
  WindGustSpeed                          0.0896
  Sunshine                               0.0694
  Cloud3pm                               0.0195
  Pressure9am                            0.0178
  MaxTemp                                0.0101

These results measure **predictive reliance**, not causal effects.
Correlated meteorological variables may also share or mask importance.

## Error Analysis and Robustness

Performance was relatively stable across the three Melbourne-area
stations in the primary 2017 test. Seasonal diagnostics were less
uniform. In the small 2017 winter subset, the global threshold detected
none of the 11 observed rainy cases, even though probability-ranking
metrics retained useful signal.

A harder **station-holdout** experiment trained the selected model on
two stations and evaluated it on the third unseen station. Average
Precision ranged from approximately **0.554 to 0.632**, indicating
useful but imperfect spatial transfer.

These diagnostics reinforce an important applied lesson: aggregate model
performance can conceal meaningful temporal or subgroup weaknesses.

## Business Analytics Relevance

Although rainfall is the application domain, the analytical framework is
directly transferable to business problems such as:

-   customer churn and retention risk;
-   credit default and financial risk;
-   fraud and anomaly detection;
-   demand and inventory forecasting;
-   operational disruption and equipment failure;
-   marketing response and propensity modeling.

Across these applications, the same questions matter: **What information
is available at decision time? Is validation realistic? Which error is
more costly? Are probabilities calibrated? Does performance deteriorate
over time or across segments?**

The project therefore demonstrates not only Python model implementation,
but also the ability to connect predictive modeling with **decision
design, empirical validity, and critical interpretation**.

## Technical Skills Demonstrated

-   Python
-   pandas and NumPy
-   Matplotlib
-   scikit-learn
-   `Pipeline` and `ColumnTransformer`
-   missing-data imputation
-   categorical encoding and feature scaling
-   cyclical temporal feature engineering
-   Logistic Regression
-   Random Forest
-   Histogram Gradient Boosting
-   `GridSearchCV`
-   expanding-window temporal cross-validation
-   imbalanced-class evaluation
-   ROC and precision-recall analysis
-   probability calibration and Brier score
-   decision-threshold optimization
-   permutation feature importance
-   subgroup and robustness analysis

## Repository Structure

``` text
.
├── Predicting_Daily_Rainfall_Melbourne_Temporal_Validation_Model_Comparison_FINAL.ipynb
│   └── Fully executed technical notebook with code, outputs, tables, and figures
│
├── Predicting_Daily_Rainfall_Melbourne_Portfolio_Report.docx
│   └── Companion research-style report for academic/portfolio review
│
├── weatherAUS_2.csv
│   └── Source dataset used to reproduce the analysis
│
└── README.md
    └── Project overview and navigation
```

> **Data note:** If the source dataset is not redistributed in the
> public repository, place `weatherAUS_2.csv` locally before executing
> the notebook and document the dataset source instead.

## Reproducibility

The notebook is fully executed and contains the outputs underlying the
reported results. Preprocessing is embedded inside scikit-learn
pipelines so that imputation, scaling, and encoding are estimated only
from the appropriate training data.

For archival reproducibility, keep the dataset in the same directory as
the notebook using the filename:

``` text
weatherAUS_2.csv
```

## Limitations

-   The analysis is predictive rather than causal.
-   The Melbourne-metro focus limits geographic generalization.
-   Nearby stations may exhibit spatial dependence because they
    experience common weather systems.
-   The 2017 final test ends in June rather than covering a complete
    calendar year.
-   The winter subgroup is small and should not support strong seasonal
    conclusions.
-   Median/mode imputation is transparent and leakage-safe but does not
    model the missingness mechanism.
-   The F1-selected threshold is a statistical decision rule rather than
    an economically optimized cost function.
-   Temporal deterioration suggests that a deployed system would require
    monitoring, recalibration, and potentially periodic retraining.

## Project Provenance

This project originated from a rainfall-classification exercise
completed as part of the **IBM Data Science Professional Certificate**.

The original exercise established the technical foundation: data
preprocessing, scikit-learn pipelines, `GridSearchCV`, Random Forest and
Logistic Regression, classification metrics, and feature-importance
analysis.

For this portfolio version, the project was substantially redeveloped to
include:

-   pipeline-contained imputation instead of complete-case deletion;
-   an explicit next-day forecasting horizon;
-   chronological development, validation, and test periods;
-   expanding-year temporal cross-validation;
-   a naïve baseline and an additional gradient-boosting model;
-   Average Precision--based model selection;
-   validation-only threshold optimization;
-   probability calibration;
-   held-out permutation importance;
-   seasonal and station-level error analysis;
-   station-holdout robustness evaluation.

The original certificate results are treated as **historical
provenance**, not as results from the redesigned temporal experiment.

## Portfolio Artifacts

For academic or PhD-application review, the project is designed to be
read at three levels:

**1. README --- quick orientation**\
This page summarizes the research question, methodological design, major
results, and analytical contribution.

**2. Jupyter Notebook --- technical evidence**\
The fully executed notebook contains the complete Python implementation,
outputs, figures, hyperparameter searches, diagnostics, and reproducible
workflow.

**3. Research-Style Report --- interpretation**\
The companion report presents the motivation, methodology, empirical
findings, limitations, and relevance to business/data analytics without
duplicating the notebook cell by cell.

## References

-   Australian Bureau of Meteorology. *About rainfall data.*\
    https://www.bom.gov.au/climate/cdo/about/about-rain-data.shtml
-   Australian Bureau of Meteorology. *Climate Data Online --- rainfall
    definitions.*\
    https://www.bom.gov.au/climate/cdo/about/definitionsrain.shtml
-   scikit-learn developers. *TimeSeriesSplit.*\
    https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
-   scikit-learn developers. *Permutation feature importance.*\
    https://scikit-learn.org/stable/modules/permutation_importance.html
-   scikit-learn developers. *Probability calibration.*\
    https://scikit-learn.org/stable/modules/calibration.html
-   Breiman, L. (2001). *Random Forests.* Machine Learning, 45, 5--32.

------------------------------------------------------------------------

### Portfolio Focus

**Python • Machine Learning • Predictive Analytics • Temporal Validation
• Model Evaluation • Decision Analytics**

This repository is part of a broader portfolio demonstrating preparation
for doctoral study in **Business Analytics / Data Analytics**, with
emphasis on rigorous empirical reasoning and reproducible computational
analysis.
