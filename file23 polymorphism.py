class Ws:
    def displayinfo(self):
        print("Welcome to Ajayam world")

class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("Welcom to world of Ajayam")


obj=IIP()
obj.displayinfo()