import numpy as np
import pandas as pd 

info = np.array([10,20,30,40])
s = pd.Series(info)
print("\nValues in series =\n",s)

i = pd.Index([2,1,1,np.nan,3])
print("\nCount the values = \n",i.value_counts())


x = pd.Series(4, index=[0, 1, 2, 3])  
print ("\nprint repated numbers = \n",x)  

ser1 = pd.Series([10,1,3,6])
ser2 = pd.Series([10,5,6,9])
print("\nSeries 1 = \n",ser1)
print("\nSeries 2 = \n",ser2)

union = pd.Series(np.union1d(ser1, ser2))
print("\n Union = \n",union)

intersection = pd.Series(np.intersect1d(ser1, ser2))
print("\nintersection = \n",intersection)

notcommon = union[~union.isin(intersection)]
print("\nNotcommom = \n",notcommon) 
