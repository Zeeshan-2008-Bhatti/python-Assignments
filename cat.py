import Animal
class Cat(Animal.Animal):

    def Walk(self):
        print(self.name,"is walking")



cat = Cat("kt")
cat.Eat()
cat.Speake()
cat.Walk()