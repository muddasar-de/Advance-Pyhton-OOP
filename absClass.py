from abc import ABC,abstractclassmethod

class Parent(ABC):

    @abstractclassmethod
    def method1(self):
        pass
    @abstractclassmethod
    def method2(self):
        pass