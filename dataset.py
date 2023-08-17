import pandas as pd

data = pd.read_csv("C:/Users/SPTINT-14/Downloads/Athlete_events_outliers (2).csv")
print(data)
print(data.head(5))
print(data.tail(10))
print(data.info())
print(data["Team"].head(5))
print(data.dtypes)
print(data.count())
