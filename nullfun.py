
import pandas as pd
import numpy as np

dict={' first score':[10,20,np.nan,30],
      'second score':[np.nan,10,20,30],
      'third score':[np.nan,20,30,np.nan]}

data=pd.DataFrame(dict)
print(data)

print(data.isnull())
print(data.notnull())

print(data.fillna(20))
print(data.fillna(method="pad"))
print(data.fillna(method="bfill"))
print(data.replace(to_replace=np.nan,value=-99))

