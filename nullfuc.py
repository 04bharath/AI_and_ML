import pandas as pd
import numpy as np 

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/python/taitanic2.csv",index_col=('Cabin'))[:150]
print(data)
data1=pd.DataFrame(data)
print(data1)
print(data.isnull())
print(data.notnull())
print(data.fillna(0))
print(data.fillna(method="pad"))
print(data.fillna(method="bfill"))
print(data.replace(to_replace=np.nan,value=-100))
print(data.dropna())
print(data.dropna(how="all"))
