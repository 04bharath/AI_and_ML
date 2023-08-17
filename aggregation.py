import numpy as np

arr = np.array([[2,3,4],[1,6,5]])
print("Sum of array is = ",arr.sum())
print("Maxium of array is = ",arr.max())
print("Minum of array is = ",arr.min())
print("\nElements of array = \n",arr)
print("Maxium of array is = ",arr.max(axis=1))
print("Minium of array is = ",arr.min(axis=1))
print("\nCumsum of array is = \n",arr.cumsum(axis=1))
print("Average of array is = ",np.average(arr))

