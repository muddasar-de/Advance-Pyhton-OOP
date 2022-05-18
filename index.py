# # ---------------------- Creating Class and Instance ------------------------

# class Person:

#     # ------ Class Variable -----
#     gender = "Male"

#     # -------- Constructor -------
#     def __init__(self, name, age, profession) -> None:
        
#         # --------- Instance Varibles ---------
#         self.name = name
#         self.age = age
#         self.profession = profession
    
#     # ---------- Instance Methods ----------
#     def info(self):
#         print(f"I am {self.name} and I am {self.age} years old with gender {Person.gender}." )
    
#     def work(self):
#         print(f"I am a {self.profession} in Assistech Solutions")

#     # -------- Class Method ---------
#     @classmethod
#     def change_gender(cls,new_gender_value):
#         cls.gender = new_gender_value
#         return(cls.gender)
    

# me = Person("Muddasar",23,"Python Developer" )
# Person.change_gender("Female")
# me.info()
# me.work()
# me.name="Kashif"
# me.info()
# del me
# me.info()   #error
# print(Person.gender)



# ------------- Constructor Chaining -------------

# class Vehicle:
#     # Constructor of Vehicle
#     def __init__(self, engine):
#         print('Inside Vehicle Constructor')
#         self.engine = engine
#         print(self.engine)

# class Car(Vehicle):
#     # Constructor of Car
#     def __init__(self, engine, max_speed):
#         super().__init__(engine)
#         print('Inside Car Constructor')
#         self.max_speed = max_speed
#         print(self.max_speed)

# class Electric_Car(Car):
#     # Constructor of Electric Car
#     def __init__(self, engine, max_speed, km_range):
#         super().__init__(engine, max_speed)
#         print('Inside Electric Car Constructor')
#         self.km_range = km_range


# # Object of electric car
# ev = Electric_Car('1500cc', 240, 750)
# print(f'Engine={ev.engine}, Max Speed={ev.max_speed}, Km range={ev.km_range}')



# -------------------- Destructor ---------------------
# import time
# class Assistech:
    
#     # constructor
#     def __init__(self, location, employees) -> None:
#         self.loc = location
#         self.emp = employees
#         print(self.loc,self.emp)
    
#     # destructor
#     def __del__(self):
#         print("Destroyed")

# class Project(Assistech):
#     def __init__(self,name, working_employees) -> None:
#         super().__init__("NSTP",working_employees)
#         self.name = name

#     def __del__(self):
#        pass

# obj = Assistech("NSTP",26)
# obj1 = obj

# time.sleep(2)
# del obj

# print(obj1.emp)

# del Assistech


# import time

# class Student:

#     # constructor
#     def __init__(self, name):
#         print('Inside Constructor')
#         self.name = name

#     def show(self):
#         print('Hello, my name is', self.name)

#     # destructor
#     def __del__(self):
#         print('Object destroyed')

# # create object
# s1 = Student('Emma')
# # create new reference
# # both reference points to the same object
# s2 = s1
# s1.show()

# # delete object reference s1
# del s1

# # add sleep and observe the output
# time.sleep(5)
# print('After sleep')
# s2.show()



# ---------------------- Inheritance ------------------------ 

# ------------------ Single Inheritance -------------



# Base Class


class Vehicle:
    _sch = "PAK"
    def __init__(self) -> None:
        self.name = "Muddasar"
        self.__age = 23
    def Vehicle_info(self):
        print('Inside Vehicle class')
        
# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Create object of Car
car = Car()

veh = Vehicle()
print(veh._sch)
# access Vehicle's info using car object
car.Vehicle_info()
car.car_info()
# print(car.__age)
print(car._sch)
# print(car.age)


# ------------------ Multiple Inheritance -------------

# Parent class 1
# from operator import le


# class Person:
#     def person_info(self, name, age):
#         print('Inside Person class')
#         print('Name:', name, 'Age:', age)

# # Parent class 2
# class Company(Person):
#     def company_info(self, company_name, location):
#         print('Inside Company class')
#         print('Name:', company_name, 'location:', location)

# # Child class
# class Employee(Company, Person):
#     def Employee_info(self, salary, skill):
#         print('Inside Employee class')
#         print('Salary:', salary, 'Skill:', skill)

# # Create object of Employee
# emp = Employee()
# print(Employee.mro())

# # access data
# emp.person_info('Jessa', 28)
# emp.company_info('Google', 'Atlanta')
# emp.Employee_info(12000, 'Machine Learning')


# # ------------------ Multilevel Inheritance -------------

# # Base class
# class Vehicle:
#     def Vehicle_info(self):
#         print('Inside Vehicle class')

# # Child class
# class Car(Vehicle):
#     def car_info(self):
#         print('Inside Car class')

# # Child class
# class SportsCar(Car):
#     def sports_car_info(self):
#         print('Inside SportsCar class')

# # Create object of SportsCar
# s_car = SportsCar()

# # access Vehicle's and Car info using SportsCar object
# s_car.Vehicle_info()
# s_car.car_info()
# s_car.sports_car_info()


# # ------------------ Hierarichical Inheritance -------------

# class Vehicle:
#     def info(self):
#         print("This is Vehicle")

# class Car(Vehicle):
#     def car_info(self, name):
#         print("Car name is:", name)

# class Truck(Vehicle):
#     def truck_info(self, name):
#         print("Truck name is:", name)

# obj1 = Car()
# obj1.info()
# obj1.car_info('BMW')

# obj2 = Truck()
# obj2.info()
# obj2.truck_info('Ford')


# # ------------------ Hybrid (Diamond) Inheritance -------------


# class Vehicle:
#     def vehicle_info(self):
#         print("Inside Vehicle class")

# class Car(Vehicle):
#     def car_info(self):
#         print("Inside Car class")

# class Truck(Vehicle):
#     def truck_info(self):
#         print("Inside Truck class")

# # Sports Car can inherits properties of Vehicle and Car
# class SportsCar(Car, Vehicle):
#     def sports_car_info(self):
#         print("Inside SportsCar class")

# # create object
# s_car = SportsCar()

# s_car.vehicle_info()
# s_car.car_info()
# s_car.sports_car_info()

# --------- use of super function ----------- 

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name  = name
#         self.age = age
    
#     def display(self):
#         print(f"I am {self.name} and I am {self.age} years old.")

# class Department:
#     def __init__(self, department) -> None:
#         self.dep = department
#     def show(self):
#         print(self.dep)

# class Student(Person, Department):
#     def __init__(self,name,age, fees, subject, dep) -> None:
#         super().__init__(name, age)
#         super().__init__(dep)
#         self.fees = fees
#         self.subject = subject 
#         self.show() 
#     def print(self):
#         print(self.name,self.age)


        
# s1 = Student("Muddasar",23, 15000,"Computer", "CS" )



# ---------------------- Inheritance ------------------------ 

# ---------------- Method Resolution Order (MRO) ------------------- 

# class A:

#     def __init__(self,order) -> None:
#         self.order = order
#     def show(self):
#         print("This is Class A")


# class B(A):
#     def display(self):
#         print("This is Class B")


# class C(B,A):
#     def count(self):
#         print("This is Class C")


# obj = C(123)
# print(obj.order)
# obj.display()
# obj.show()
# print(C.mro())


# ---------------- Polynorphsim ----------------
# class Shopping:
#     def __init__(self, basket, buyer):
#         self.basket = list(basket)
#         self.buyer = buyer

#     def __len__(self):
#         print('Redefine length')
#         count = len(self.basket)
#         # count total items in a different way
#         # pair of shoes and shir+pant
#         return count * 2

# shopping = Shopping(['Shoes', 'dress'], 'Jessa')
# print(len(shopping))


# ----------- Polymorphism in built in functions ----------

# class cars:
#     def __init__(self,carList,az) -> None:
#         self.list  = carList
    
#     def __len__(self):
#         count = len(self.list)
#         return count*2

# obj = cars(["Mercedes","BMW","HONDA"],"asd")
# obj1 = ["Mercedes","BMW","HONDA","asd"]
# print(len(obj))

# ----------- Polymorphism in class methods ----------


# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")

#     def max_speed(self):
#         print("Max speed 350")

# class BMW:
#     def fuel_type(self):
#         print("Diesel")

#     def max_speed(self):
#         print("Max speed is 240")

# ferrari = Ferrari()
# bmw = BMW()

# # iterate objects of same type
# for car in (ferrari, bmw):
#     # call methods without checking class of object
#     car.fuel_type()
#     car.max_speed()


# -----------Polymorphism with Function and Objects--------------

# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")

#     def max_speed(self):
#         print("Max speed 350")

# class BMW:
#     def fuel_type(self):
#         print("Diesel")

#     def max_speed(self):
#         print("Max speed is 240")

# ferrari = Ferrari()
# bmw = BMW()

# # iterate objects of same type
# for car in (ferrari, bmw):
#     # call methods without checking class of object
#     car.fuel_type()
#     car.max_speed()


# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")

#     def max_speed(self):
#         print("Max speed 350")

# class BMW:
#     def fuel_type(self):
#         print("Diesel")

#     def max_speed(self):
#         print("Max speed is 240")

# # normal function
# def car_details(obj):
#     obj.fuel_type()
#     obj.max_speed()

# ferrari = Ferrari()
# bmw = BMW()

# car_details(ferrari)
# car_details(bmw)


# --------------- Encapsulation ---------------- 

# A normal creating class with declaring varibales and methods leads to encapsulation

# class Employee:
#     # constructor
#     def __init__(self, name, salary, project):
#         # data members
#         self.name = name
#         self.salary = salary
#         self.project = project

#     # method
#     # to display employee's details
#     def show(self):
#         # accessing public data member
#         print("Name: ", self.name, 'Salary:', self.salary)

#     # method
#     def work(self):
#         print(self.name, 'is working on', self.project)

# # creating object of a class
# emp = Employee('Jessa', 8000, 'NLP')

# # calling public method of the class
# emp.show()
# emp.work()



#------------------ Access Modifiers ----------------------

# --------- public member --------
# class Employee:
#     def __init__(self, name, salary) -> None:
#         self.salary = salary
#         self.name = name
    
#     def work(self):
#         print(f"{self.name} is doing job at {self.salary} salary package.")

# emp = Employee("Muddasar", 15000)

# # instance varibales are accessible outside and inside the class

# print(f"{emp.name} {emp.salary}")

# emp.work()


# ------------- protected member ----------

# class Person:
#     def __init__(self,name, salary) -> None:
#         self._salary = salary
#         self.name = name
#     def work(self):
#        print(f"{self.name} is doing job at {self.salary} salary package.")

# class Employee(Person):
#     def __init__(self, name, salary) -> None:
#         super().__init__(name, salary)
        
## protected member can be access inside or outside the class as well as thier subclasses.

# emp = Employee("Muddasar", 15000)
# print(emp._salary, emp.name)


# ------------- private member ----------

# class Person:
#     def __init__(self,name, salary) -> None:
#         self.__salary = salary
#         self.name = name
#     def _work(self):
#        print(f"{self.name} is doing job at {self.__salary} salary package.")

# class Employee(Person):
#     def __init__(self, name, salary) -> None:
#         super().__init__(name, salary)
        
# # privat member is only accessible with in the class scope where it is declared.
# emp = Employee("Muddasar", 15000)
# # print(emp.__salary, emp.name)
# emp._work()

# per = Person("Muddasar", 1500000)

# print(per.__salary)


# ----------------- How to access Private Members --------------- 

# Method 1: Public method to access private members

# Example: Access Private member outside of a class using an instance method


# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary

#     # public instance methods
#     def show(self):
#         # private members are accessible from a class
#         print("Name: ", self.name, 'Salary:', self.__salary)

# # creating object of a class
# emp = Employee('Jessa', 10000)

# # calling public method of the class
# emp.show()


# #Method 2: Name Mangling to access private members

# class Person:
#     def __init__(self, name) -> None:
#         self.__name = name
    
# class Employee(Person):
#     def __init__(self, name) -> None:
#         super().__init__(name)
    
# emp = Employee("Muddasar")

# print(emp._Person__name)


# from time import sleep


# class Person():
#     def __init__(self,name,salary) -> None:
#         self.n = name
#         self.s = salary

# class Employee(Person):
#     def __init__(self, name, salary,role) -> None:
#         super().__init__(name,salary)
#         self.r = role


#     def __del__(self):
#         print("object destroyed")
# obj = Employee("Muddasar",15000, "JD")
# obj1 = obj
# print(obj.n)
# sleep(5)
# print(obj1.n)
# del obj
# print(obj1.r)



# -------------------Abstraction---------------
# from abc import ABC,abstractclassmethod

# from numpy import number

# class Parent(ABC):

#     @abstractclassmethod
#     def pqr(self):
#         pass

# class Child(Parent):

#     def pqr(self):
#         print("PQR")

# obj = Child()
# obj.pqr()



# ----------------------- Advance Python --------------------------

# Iterators:

# numbers = [1, 2, 3]

# iterator = iter(numbers)
# print(type(iterator))


# class PowTwo:
#     """Class to implement an iterator
#     of powers of two"""

#     def __init__(self, max=0):
#         self.max = max

#     def __iter__(self):
#         self.n = 0
#         return self

#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration


# # create an object
# numbers = PowTwo(3)

# # create an iterable from the object
# i = iter(numbers)

# # Using next to get to the next iterator element
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))



# ------------------- Generators ------------------

# A simple generator function
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n

#     n += 1
#     print('This is printed second')
#     yield n

#     n += 1
#     print('This is printed at last')
#     yield n


# # Using for loop
# for item in my_gen():
#     print(item)


# Python Generators with a Loop

# def rev__str(str):
#     for ch in range(len(str)-1,-1,-1):
#         yield str[ch]

# print(rev__str("Hellow"))

# for chr in rev__str("Hellow"):
#     print(chr)


# ------ Pipeline Calling Generators --------

# def fib(max):
#     x, y =0,1
#     for i in range(max):
#         # print("fib",i)
#         x, y = y, y+1
#         print("fib",x)
#         yield x

# def square(nums):
#     print(nums)
#     for num in nums:
#         print("Square",num)
#         yield num**2

# print("Sum",sum(square(fib(10))))


# ------------- Decorators --------------

#  -------------- scenario 1 ---------------
# def add(num):
#     return num +1

# def operate(func,x):
#     print(func)
#     return func(x)

# print(operate(add,4))



# ---------- scenario 2 ------------


# def operate(n):
#     print(n)

    
#     def add(num):
#         return num +1
#     return add

# oper = operate(2)

# print(oper(4))


# ------- Realtime Examples ---------

# def only_customer(func):

#     def decorator(user):
#         if(user == "muddasar"):
#             print("True")
#             return func(user)
#         else:
#             print("False")

#     return decorator


# @only_customer
# def login(user):
#     print(user)
#     print("loged in")

# login("muddasar")



# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner


# @smart_divide
# def divide(a, b):
#     print(a/b)

# divide(2,7)

# ------------------------ *args, **kwargs -----------------


# def treverse(*args, **kwargs):
#     # print(args[0])
#     print(kwargs["a"])
#     for i in args:
#         print(i)



# asd = '''Muddasa
# asd
# asd         asd'''
# asdwq = 2
# treverse(asd,asdwq,2, a=1,b=4,c=5,d=6,e=7 )

# class Class1():
#     def __init__(self) -> None:
#         self.name = "Muddasar"
    
