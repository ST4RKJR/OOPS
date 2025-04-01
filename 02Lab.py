class Dog:
    def __init__(self,name,age,breed,gender,color,friend):
        self.name = name
        self.age = age
        self.breed = breed
        self.gender = gender
        self.color = color
        self.friend = friend

    def introduce(self):
        if self.friend:
            print(f"My Dog's name is {self.name}. \nMy Dog's age is {self.age}. \nMy Friend Name is {self.friend.name}")
        else:
            print(f"My Dog's name is {self.name}. \nMy Dog's age is {self.age}. \nI Dont Have any Friend")
              
    def bark(self):
        print("Woof Woof")
    def eat(self):
        print("I Love to eat pedigree")
    # def Name(self):
    #     return self.Name
    # def Age(self):
    #     return self.age
    # def Breed(self):
    #     return self.breed
    # def Gender(self):
    #     return self.gender
    # def color(self):
    #     return self.color
    # def Owner(self):
    #     return self.owner
    

