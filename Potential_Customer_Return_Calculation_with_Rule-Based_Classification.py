# **************************
# Business Problem:
# Our company aims to create new customer personas based on certain characteristics of our current customers, using a level-based approach.
# After forming segments based on these new personas, we intend to predict how much a potential new customer in each segment might generate in terms of revenue for the company.
# For instance, we want to determine the average revenue a 25-year-old male IOS user from Turkey might bring to the company."
# **************************

# **************************
# Dataset Story:
# The 'Persona.csv' dataset contains the prices of products sold by an international gaming company and certain demographic information about the customers who purchased these products.
# The dataset is composed of records created with each sale transaction. Hence, the table is not deduplicated.
# In other words, a user with specific demographic features might have made multiple purchases."
# **************************

# **************************
# VARIABLES
# SOURCE     -   The type of device the customer connected from
# SEX        -   The gender of the customer
# COUNTRY    -   The country of the customer
# AGE        -   The age of the customer
# PRICE      -   The amount the customer spent
# **************************

# **************************
# Project Tasks
# Task 1: What are the average revenues in the COUNTRY, SOURCE, SEX, AGE breakdown?
# Task 2: Sort the output by PRICE.
# Task 3: Convert index names to variable names.
# Task 4: Convert the Age variable to a categorical variable and add it to agg_df.
# Task 5: Define new level-based customers (personas).
# Task 6: Segment the new customers (personas).
# Task 7: Classify the incoming customers and estimate how much revenue they might generate.

import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

# Suppressing all warnings of type 'Warning' to keep the output clean
warnings.simplefilter(action='ignore', category=Warning)

df = pd.read_csv('persona.csv')



# to get an initial understanding of the data's structure, its content, and if there are any missing values that need to be addressed.
def sum_df(dataframe, head=6):
    print("~~~~~~~~~~|-HEAD-|~~~~~~~~~~ ")
    print(dataframe.head(head))
    print("~~~~~~~~~~|-TAIL-|~~~~~~~~~~ ")
    print(dataframe.tail(head))
    print("~~~~~~~~~~|-TYPES-|~~~~~~~~~~ ")
    print(dataframe.dtypes)
    print("~~~~~~~~~~|-SHAPE-|~~~~~~~~~~ ")
    print(dataframe.shape)
    print("~~~~~~~~~~|-NA-|~~~~~~~~~~ ")
    print(dataframe.isnull().sum())
    print("~~~~~~~~~~|-QUANTILES-|~~~~~~~~~~ ")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
    print("~~~~~~~~~~|-NUMERIC COLUMNS-|~~~~~~~~~~ ")
    print([i for i in dataframe.columns if dataframe[i].dtype != "O"])

sum_df(df)

#**********************************************************************************
# Task 1: What are the average revenues in the COUNTRY, SOURCE, SEX, AGE breakdown?
#**********************************************************************************

df.groupby(["COUNTRY", "SOURCE","SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)

#*************************************
# # Task 2: Sort the output by PRICE.
#*************************************

agg_df = df.groupby(["COUNTRY", "SOURCE","SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)

#***********************************************
# Task 3: Convert index names to variable names.
#***********************************************

agg_df.reset_index(inplace=True)

#*********************************************************************************
# Task 4: Convert the Age variable to a categorical variable and add it to agg_df.
#*********************************************************************************

# Convert the numerical Age variable into a categorical one.
# Create intervals that you find convincing.
# For instance: '0_18', '19_23', '24_30', '31_40', '41_70'

# Let's specify the break points for the AGE variable:
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]

# Specify the labels corresponding to the break points:
mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]

# Bin the age:
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()


#*****************************************************
# Task 5: Define new level-based customers (personas).
#*****************************************************

agg_df["customers_level_based"] = [i[0].upper() + "_" +
                                   i[1].upper() + "_" +
                                   i[2].upper() + "_" +
                                   i[5].upper()
                                   for i in agg_df.values]


agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

#**********************************************
# Task 6: Segment the new customers (personas).
#**********************************************

agg_df["SEGMENT"] = pd.cut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])

agg_df.groupby("SEGMENT").agg({"PRICE" : ["mean", "max", "sum"]})

agg_df = agg_df.reset_index()

#*******************************************************************************************
# Task 7: Classify the incoming customers and estimate how much revenue they might generate.
#*******************************************************************************************

# What segment does a 33-year-old Turkish woman using ANDROID belong to and what is the expected average revenue from her?
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

# What segment does a 35-year-old French woman using IOS belong to and what is the expected average revenue from her?
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]


def predict(i):
    new_customer = agg_df[agg_df["customers_level_based"] == i]
    segment = new_customer["SEGMENT"].mode()[0]
    price =new_customer["PRICE"].mean()
    print(f"The New customer's segment = {segment}, Estimated spending {price} ")

predict("FRA_IOS_FEMALE_31_40")


