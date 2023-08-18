lar=lambda x,y : x if(x>y) else y
print("biggest number = ",lar(2,3))

lst = [5,6,8,4,2]
x = list(map(lambda x: x+5,lst))
print("Addition of each number =",x)

lst2 = [0,5,8,9,10,6,55,63]
a = list(filter(lambda x:x%2,lst2))
print("odd numbers = ",a)

lst3 = [0,5,8,9,10,6,55,63]
a = list(filter(lambda x:x%2==0,lst3))
print("even numbers = ",a)

from functools import reduce
lst4 = [5,8,6,45,85]
b = reduce(lambda x,y:x+y,lst4)
print('Reduce list = ',b)

lst4 = [5,8,6,45,85]
b1 = reduce(lambda x,y:x if (x>y) else y,lst4)
print("Largest number in list = ",b1)

lst5 = [5,6,8,4,2]
x1 = list(map(lambda x: x*x,lst5))
print("squre of each number =",x1)


