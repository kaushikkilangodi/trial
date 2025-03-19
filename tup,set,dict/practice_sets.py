#adding element into the empty set

animal=set()
animal.add('dog')
animal.add('cat')
print(animal)

number={1,2,3,4,5}
number.remove(2)
print(number)

colors={'red','green','blue'}
if 'red' in colors:
    print("present")
    print('*************************************************************')


x={1,2,3,4}
y={5,6,7}
x.update(y)
print(x)