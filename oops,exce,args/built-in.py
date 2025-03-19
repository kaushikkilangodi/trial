numbers=[1,2,3,4,5]

print(len(numbers))
print(max(numbers))
print(sum(numbers))

x=dict(x=1,y="name",z='xyz')
print(x)
print('*****************************************')


a=list((1,2,3,4))
b=tuple(a)
s=slice(2)
print("list",a)
print("tuple",b)
print("sliced",a[s])
print('*****************************************')


age=[10,15,18,23,33,45]

def function(x):
    if x>=18:
        return True
    else:
        return False
people=filter(function,age)

for x in people:
    print(x)


f=[3,6,1,2,9,5]
b=sorted(f)
print(b)

x=pow(2,3)
print(x)