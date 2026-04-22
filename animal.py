class Animal:
    name=""
    sound=""
    eat=""
    def __init__(self,name,sound,eat):
        self.name = name
        self.sound=sound
        self.eat=eat
    def speak(self):
        print(self.name," says ",self.sound, " and eats ",self.eat)
dog= Animal("Dog","woef","chicken")
cat=Animal("cat","Meow","fish")
dog.speak()
cat.speak()

