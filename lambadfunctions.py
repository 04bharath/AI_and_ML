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

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l3 = [8,6,5,4,1]
l = list(map(lambda x,y,z:x+y+z,l1,l2,l3))
print("Add the 3 list=",l)

fruits = ['mango','orange','apple','kiwi']
l1 = list(filter(lambda x:'g' in x,fruits))
print("G in the list = ",l1)

fruits = ['mango','orange','apple','kiwi']
l2 = list(filter(lambda x:'g' not in x,fruits))
print("G not in list = ",l2)


