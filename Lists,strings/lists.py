#create

a=[1,2,3,4,5,6]
b=['a',2,True,'c',4]

#Accessing using index
print(a[0])
print(b[3])
print('accessing last element',b[-1])

#adding to the lsit

a.append(10)
print("after appending",a)

a[1]=10
print("Updated value",a)

a.remove(10)
print("removing element",a)

a.pop(1)
print("popped ele",a)

#using for loop

# for i in a:
#     print(i)

#user input

# res= input("enter the numbers").split()
# print("in list",res)

#using map

res=list(map(int,input("enter the numbers").split()))
print("list",res)

# r1=10
# res=list(range(r1))
# print(res)

r2=5
res=[i for i in range(r2)]
print(res)