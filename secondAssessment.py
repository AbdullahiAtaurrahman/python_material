class User:
    def __init__(self, firstName, lastName, age, regNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.regNumber = regNumber

    def Name(self):
        return f"My name is ${self.firstName} ${self.lastName}"