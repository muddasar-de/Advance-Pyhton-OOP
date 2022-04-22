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


import time

class Student:

    # constructor
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name

    def show(self):
        print('Hello, my name is', self.name)

    # destructor
    def __del__(self):
        print('Object destroyed')

# create object
s1 = Student('Emma')
# create new reference
# both reference points to the same object
s2 = s1
s1.show()

# delete object reference s1
del s1

# add sleep and observe the output
time.sleep(5)
print('After sleep')
s2.show()