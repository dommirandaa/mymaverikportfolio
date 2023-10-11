#EDA Tasks - Dom
import numpy as np
import pandas as pd
import warnings #supress warnings
warnings.filterwarnings('ignore')
np.random.seed(7)

#import excel file
df = pd.read_csv("time_series_data_msba.csv")
print(df.head())

df1 = pd.read_csv("qualitative_data_msba.csv")
print(df1.head())

#data preprocessing
df = df.sort_values(by='calendar.calendar_day_date')
df1 = df1.sort_values(by='open_year')

#DESCRIPTION OF DATA
#In the time series csv, the data available for the project is sorted by the calendar day date and reflects the daily inside sales that inlcudes food service, disel, and unleaded sales.
#In the qualitative csv, the data available for the project provides specs and details for the given gas station store. A variety of food options such as pizza, cinnabon, bonfire grill, lottery, freal, etc. have 'yes' and 'no' variables. While other features indicate mile radious to the store site.

#MISSING DATA
#count of missing values for each dataset
print(df.isna().sum())
print(df1.isna().sum())
#The scope of the missing data includes columns such as traditional forecourt type, HI flow RV lanes, and RV lanes have missing values.The proposed solution is to fix the missing values is to fill the NaN with most frequent (mode) values.

#fix missing values
#filling NaN with mode
df1 = df1.fillna(df1.mode().iloc[0])
#new count of missing values
print(df1.isnull().sum())
print(df1)

