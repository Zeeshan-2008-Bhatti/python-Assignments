class person:
    name="zeeshan ali"
    age=18
    def introduction(self,name,age):
        print("nameis: " ,name)
        print("age is: ",age)
        print("Hello, my name is", self. name,"My age is: ",self.age)

person1=person()
print(person1.name)
print(person1.age)
person1.introduction("zeeshan",18)

