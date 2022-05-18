from unicodedata import name
from index import Class1
class A(Class1):
    
    def __init__(self) -> None:
        super().__init__()

    def show(slef):
        print("This is class A")
        print(super.name)
    
    def method2():
        print("Method 2 called...")

obj = A
# obj.method1()
obj.show()