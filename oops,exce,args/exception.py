x=5
try:
    print(x)
except:
    print("this is an error")
finally:
    print("this final exception")


try:
    print(1/2)
except:
    print("zero division error")