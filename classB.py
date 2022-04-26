from classA import A 
class B(A):
    def show(self):
        print("This is class B")
        super().show()
    
    

obj = B()
obj.show()