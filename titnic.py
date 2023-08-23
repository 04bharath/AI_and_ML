import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/SPTINT-14/Desktop/dataset/titanic.csv")
print(data.info())
print(data.isnull().sum())
print("\nLenth of data = \n",len(data))
print(data['Survived'].value_counts().plot(kind='bar'))
print(data['Survived'].value_counts())
print(data[data['Sex']=='female']['Survived'].value_counts().plot(kind='hist'))

