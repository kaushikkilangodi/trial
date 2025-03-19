class Add:
    @staticmethod
    def add(a,b):
        return a+b
    
print(Add.add(3,4))


# using static()

class Add:
    def add(a,b):
        return a+b
    
    add=staticmethod(add)

print(Add.add(2,3))
print("**************************")


#

class Calculator:
    @staticmethod
    def multiply(a,b):
        return a * b
    
    def add(a,b):
        return a+b
    
res=Calculator.multiply(2,3)
print(res)

res2=Calculator.add(2,2)
print(res2)
# res2=Calculator()
# res2.add(2,2)
# print(res2.add(2,2))
    
class Calculator:
    def __init__(self, value):
        self.value = value  # Instance attribute
 
    def add(self, x):
        self.value += x  # Modifies the instance's state
        return self.value
 
    @staticmethod
    def subtract(x, y):
        return x - y  # Static method: No access to instance data
 
# Instance Method usage
calc = Calculator(10)
print(calc.add(5))  # Output: 15 (adds 5 to the instance's value)
 
# Static Method usage
print(Calculator.subtract(18, 8))  # Output: 5 (static method, no instance needed)