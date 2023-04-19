class A:
    def diaplayA(self):
        print("Welcome to Ajayam A")

class B():
    def displayB(self):
        print("Welcome to Ajayam B")

class C(A,B):
    def diaplayC(self):
        print("Welcome to Ajayam C")


obj=C()
obj.diaplayA()
obj.displayB()
obj.diaplayC()