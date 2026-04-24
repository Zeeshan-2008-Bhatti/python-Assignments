class Animal:
    name = ""
    sound = ""
    eat = ""

    def __init__(self,name):
        self.name = name
    
    def Speake(self):
        print(self.name,"makes a sound.")

    def Eat(self):
        print(self.name,"is eating")

