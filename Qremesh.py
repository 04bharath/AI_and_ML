import pandas as pd

d = {'Days':[1,2,3,4,5,6,7,8,9,10],'Steps':[43335,9552,7332,4504,5335,7552,8332,6504,8965,7689]}
data = pd.DataFrame(d)
print(data)

data['Steps']=data['Steps']+10000
print("\nAfter adding 10000 = \n",data)
a = data[data['Steps']>7000]['Days']
print("\nGreater than 7000 = \n",list(a))
