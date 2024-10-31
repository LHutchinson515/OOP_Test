class Person():
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height

# defines a class of a person with some characteristics 

    def introduce(self):
        print (f"my name is {self.name}, I am {self.age}, and I am {self.height}")

# gives a way to apply the information when called on to form a sentence with the information

