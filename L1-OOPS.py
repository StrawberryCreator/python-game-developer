print ("="*50)

#function

def chatbot ():
    print ("Hello, i am a chatbot!")
    print ("What is your name?")
    name = input()
    print ("Hello", name)

chatbot ()

print ("-"*50)

#create a student class

class student:
    def __init__ (self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.teacher = "Shirin"
    def studentDetails (self):
        print (f"name {self.name}")
        print (f"age {self.age}")
        print (f"grade {self.grade}")
        print (f"teacher {self.teacher}")

student1 = student ("Sebbe", "12", "7.6")
student1.studentDetails ()
print ("- "*25)
print (student1.name)
student1.teacher = "Milou"
print ("- "*25)
student1.studentDetails ()

print ("-"*50)

#create a fruit class

class fruit:
    def __init__(self, name, amount, size, shape, taste):
        self.name = name
        self.amount = amount
        self.size = size
        self.shape = shape
        self.taste = taste
    def fruitDetails (self):
        print (f"name {self.name}")
        print (f"amount {self.amount}")
        print (f"size {self.size}")
        print (f"shape {self.shape}")
        print (f"taste {self.taste}")

fruit1 = fruit ("strawberry", 2, "small", "triangle", "sweet")
fruit1.fruitDetails ()
fruit1.amount = 5
print ("- "*25)
fruit1.fruitDetails ()

print ("="*50)
