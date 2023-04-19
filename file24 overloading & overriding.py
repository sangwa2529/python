class Area:
    def find_area(self,x=None, y=None):
        if x!=None and y!=None:
            print("side of the Ractangle is: ", x, " & ", y )
            print("Area of Ractangle: = ", x*y)

        elif x!=None:
            print("Side of the Square is: ", x)
            print("Area of Square: = ", x*x)

        else: print("Nothing value selected")


obj=Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)