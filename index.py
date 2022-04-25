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

# Base class
# class Vehicle:
#     def Vehicle_info(self):
#         print('Inside Vehicle class')

# # Child class
# class Car(Vehicle):
#     def car_info(self):
#         print('Inside Car class')

# # Create object of Car
# car = Car()

# # access Vehicle's info using car object
# car.Vehicle_info()
# car.car_info()


# ------------------ Multiple Inheritance -------------

# Parent class 1
class Person:
    def person_info(self, name, age):
        print('Inside Person class')
        print('Name:', name, 'Age:', age)

# Parent class 2
class Company(Person):
    def company_info(self, company_name, location):
        print('Inside Company class')
        print('Name:', company_name, 'location:', location)

# Child class
class Employee(Company, Person):
    def Employee_info(self, salary, skill):
        print('Inside Employee class')
        print('Salary:', salary, 'Skill:', skill)

# Create object of Employee
emp = Employee()
print(Employee.mro())

# access data
emp.person_info('Jessa', 28)
emp.company_info('Google', 'Atlanta')
emp.Employee_info(12000, 'Machine Learning')


# ------------------ Multilevel Inheritance -------------

# Base class
class Vehicle:
    def Vehicle_info(self):
        print('Inside Vehicle class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')

# Child class
class SportsCar(Car):
    def sports_car_info(self):
        print('Inside SportsCar class')

# Create object of SportsCar
s_car = SportsCar()

# access Vehicle's and Car info using SportsCar object
s_car.Vehicle_info()
s_car.car_info()
s_car.sports_car_info()


# ------------------ Hierarichical Inheritance -------------

class Vehicle:
    def info(self):
        print("This is Vehicle")

class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)

class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)

obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')


# ------------------ Hybrid (Diamond) Inheritance -------------


class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside Car class")

class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

# Sports Car can inherits properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")

# create object
s_car = SportsCar()

s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()

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