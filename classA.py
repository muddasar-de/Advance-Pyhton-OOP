from absClass import Parent
class A(Parent):
    def show(slef):
        print("This is class A")
    
    def method2():
        print("Method 2 called...")

obj = A
# obj.method1()
obj.method2()