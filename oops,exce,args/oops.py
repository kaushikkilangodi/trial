class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f'name is {self.name} and age {self.age}'

p1=Person('kaushik',23)

print(p1)   #if u use __str__
# print(p1.name)
# print(p1.age)
print('*****************************************')



# creating class and objects

class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def drive(self):
        print(f'{self.name} is driving')

    def colors(self):
        print(f'the color of the car is {self.color}')

car1=Car("mustang","red")
car1.drive()
car1.colors()
print('*****************************************')

#encapsulations

class People:
    def __init__(self,name,age,balance):
        self.name=name
        self._age=age
        self.__balance=balance
    
    def get_age(self):
        return self._age

    def person(self):
        return f'the person name is {self.name} and age is {self._age}'
    
    

p1=People("kaushik",23,5000)
print(p1.name)
print(p1.get_age())
print('*****************************************')


## inheritance
class Animal:
    def __init__(self,name):
        self.name=name

    def bark(self):
        print(f'{self.name} barks')

class Dog(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color

dog=Dog("lab",'golden')
print(dog.name)
print(dog.color)     
print('*****************************************')

#polymorphism

class Dog:
    def bark(self):
        print("dog barks")

class Cat(Dog):
    def bark(self):
        print("cat dont bRK")




dog=Dog()
cat=Cat()

dog.bark()
cat.bark()
print('*****************************************')
    

from abc import ABC,abstractmethod

class Car(ABC):
    def __init__(self,model,year):
        self.model=model
        self.year=year

    @abstractmethod
    def details(Self):
        pass

    def start(self):
        print("car started")
    
    def stop(self):
        print("car is stopped")

class Mini(Car):
    def details(self):
        print("Model",self.model)
        print("year",self.year)

    def features(self):
        print("not avaialable")

class Suv(Car):
    def details(self):
        print("Model",self.model)
        print("year",self.year)
    
    def features(self):
        print("available")


car1= Mini("nano",1999)
print(car1.model)
car1.start()
car1.features( )
print(car1.year)