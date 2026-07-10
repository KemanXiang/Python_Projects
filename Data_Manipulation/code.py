# Step 1: Importing the required libraries.
# This step involves just importing the required libraries which are pandas, numpy, and CSV. These are the necessary libraries when it comes to data science.

import pandas as pd
import numpy as np
import csv

# Step 2: Getting the data-set and displaying the data-set.
# This step involves getting the data-set from a different source, and the link for the data-set is provided below. (url: https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)
df = pd.read_csv("heart_cleveland_upload.csv")
df.head(5)

# Step 3: Removing the unused or irrelevant columns
# This step involves removing irrelevant columns such as cp, fbs, thalach, and many more, and the code is pretty much self-explanatory.

to_drop = ['cp','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','condition']

# Step 4: Renaming the column names as per our convenience.
# This step involves renaming the column names because many column names are kinda confusing and hard to understand.

new_name = {'age':'Age','sex':'Sex','trestbps':'Bps','chol':'Cholesterol'}
df.rename(columns = new_name,inplace = True)
df.head()

# Step 5: Replacing the value of the rows if necessary.
# This step involves replacing the incomplete values or making the values more readable, such as in here the Sex field consists of the values 1 and 0 being 1 as Male and 0 as Female, but it often seems ambiguous for the third person, so changing the value to an understandable one is a good idea.

replace_values = {0:'F',1:'M'}
df.df.replace({"Sex":replace_values})
df.head()
















