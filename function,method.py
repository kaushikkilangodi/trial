# function
def person(name):
    return name

print(person('abc'))



#using method
class Person:
    def greet(self,name):
        self.name=name
        print(name)
    
p1=Person()
p1.greet('hi')