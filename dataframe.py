import pandas as pd
import numpy as np 

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/csv/iris.csv")
print(data)

ser1=pd.Series(data['species'])
print(ser1)
print(ser1.value_counts())

d=pd.DataFrame(ser1)
print(d)

d1=pd.DataFrame(data["petal_length"])
print(d1)
d2=pd.DataFrame(data["sepal_width"])
print(d2)
result = pd.concat([d1, d2], axis=1)
print(result)

