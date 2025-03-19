#positional arguments
print("*************************")

def greet(name,age):
    print(f'hello {name}. Your age is {age}')

greet('kaushik',23)
print("*************************")
# keyword argumnt

def greet(name,age):
    print(f'hello {name} and {age}')
print("keyword argumrnt")
greet(age=23,name='kaushik')
print("*************************")


#default argument
def add(a=2,b=4):
    sum=a+b
    print(sum)

add()
add(4)
add(6,4)
print("*************************")

#arbitary keyword

def add(*num):
    res=0
    for nums in num:
        res+=nums
    return res
print(add(1,2,3))
print(add(1,4))


#keyword arbitary

def numbers(*text,**texts,):
    print(text)
    print(texts)

numbers(1,2,a=1,b=2,c=3,d=4,)


add=lambda a,b:a+b
print(add(5,5))


res=lambda a,b:a if a>b else b  
print(res(2,8))

add=lambda a,b,c,d:a+b+c+d
print(add(1,2,3,4))