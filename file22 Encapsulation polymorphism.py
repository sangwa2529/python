class Student:
    __name="Ravi"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()


    def __displayinfo(self):
        print("Welcome to Ajayam info")


obj=Student()
