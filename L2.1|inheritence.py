#parent an child classes

#parent

class person:
    def __init__ (self, name, IDnum):
        self.name = name
        self.IDnum = IDnum
    def personDetails (self):
        print (f"name {self.name}")
        print (f"IDnum {self.IDnum}")

#child

class employee (person):
    def __init__ (self, name, IDnum, salary, position):
        person.__init__ (self, name, IDnum)
        self.salary = salary
        self.position = position
    def employeeDetails (self):
        print (self.salary)
        print (self.position)

employee_ = employee ("Rick", "2078", "1338", "cashier")
employee_.personDetails ()
employee_.employeeDetails ()