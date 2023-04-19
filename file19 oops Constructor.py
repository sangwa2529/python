class DemoClass:
    a=10
    b=40

    def __init__(self):
        print('Welcome to Ajayam world')

    def showValue(self):
        self.c = self.a*self.a
        print(self.c)

    def showValue1(self,a,b):
        print(self.b)
        print(a*b)




obj=DemoClass()
print(obj.a)
obj.showValue()
obj.showValue1(20,30)