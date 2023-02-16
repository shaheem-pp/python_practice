class teacher:
    def __init__(self, name):
        self.name = name
        print("Hi all, My name is " + self.name)

    def teach(self):
        print("I teach Computer Science")

    def call_student(self, name):
        self.name = name
        print("Hi " + self.name + ", How can I help you?")


t1 = teacher("John")
t1.teach()
t1.call_student("Joe")

t2 = teacher("Peter")
t2.teach()
t2.call_student("Jane")
