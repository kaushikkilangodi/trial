tuple=(1,2,3,4,5)
print(tuple[1])

fruits=('apple','banana','cherry')
print(len(fruits))

tuple1=(1,2,3)
tuple2=(4,5,6)
tuple1+=tuple2
print(tuple1)


numbers=(1,2,3,4,5)
if 2 in numbers:
    print('present')
else:
    print('not present')


letters=('a','b','c','d','e')
print(letters[:3])

person=('John',28,'engineer')
name,age,profesion=person
print(name)
print(age)

tuplex=(1,2,3)
tupley=(1,2,3)
if tuplex==tupley:
    print("equal")
else:
    print('not equal')