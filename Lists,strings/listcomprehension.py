# finding the squares using list comprehension

a=[1,2,3,4]
res=[y **2 for y in a]
print(res)

#finding the even values using list comprehension
a=[1,2,3,4,5,6,7,8,9,10]
res=[val for val in a if val%2==0]
print(res)

#printing numbers

a=[val for val in range(10)]
print(a)

#using nested loops
m=[(x,y) for x in range(2) for y in range(2)]
print(m)