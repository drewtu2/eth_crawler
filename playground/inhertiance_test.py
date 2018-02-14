
class Mother(object):
    
    def __init__(self):
        self.age = 40
        self.haircolor = "Brown"
    def print_haircolor(self):
        print("Mother Haircolor: " + self.haircolor)
    def print_age(self):
        print(self.age)

class Child(Mother):

    def __init__(self):
        super(Child, self).__init__()
        self.age = 10
        self.haircolor = "Blue"

    def print_haircolor(self):
        print("Child Haircolor: " + self.haircolor)

if __name__ == "__main__":
    achild = Child()
    achild.print_haircolor()
    achild.print_age()
