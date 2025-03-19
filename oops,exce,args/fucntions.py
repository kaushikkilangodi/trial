def function():
    print("this is function")

function()


def name(fname,greet):
    print(fname + ' hi')
    print(greet)

name('kaushik','goodmorning')
print('*****************************************')


def arbitary(*names):
    print("using arbitary *")
    print("the names are",names)

arbitary("abc",'def','xyz','qwe')
print('*****************************************')


def fruits(food):
    for x in food:
        print(x)

fruits(food=['apple','mango','cherry'])
print('*****************************************')


def multiply(x):
    return x*5

print(multiply(5))

def add(x,y):
    return x+y
print(add(2,3))