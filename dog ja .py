import Animal
class Dog(Animal.Animal):

    def fetch(self):
        print(self.name,"is fetching")
        

dog=Dog("puppy")
dog.Eat()
dog.Speake()
dog.fetch()