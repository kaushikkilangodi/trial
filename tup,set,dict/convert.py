# to change the values in the tuple u need to convert it to first list change the values and change back to tuple

z=('a','b','c')
a=list(z)
a[1]='z'
z=tuple(a)
print(a)
print('*************************************************************')



#apppend
b=('x','y','z')
c=list(b)
c.append('a')
b=tuple(c)
print(b)
print('*************************************************************')

#adding tuple to tuple
tuple1=('abc','xyz')
tuple2=('def','ijk')
tuple3=tuple1+tuple2
print(tuple3)
print('*************************************************************')

tz=('a','b','c','d')
for i in tz:
    print(i)


# count()
t=(1,2,3,4,4,5)
x=t.count(4)
print(x)