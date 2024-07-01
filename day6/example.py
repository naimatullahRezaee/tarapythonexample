

class Employee:
    id = 0
    name = ''
    lastname = ''
    age = 0
    salary = 0

    def __init__(self,id,name,lastname, age,salary):
        self.id = id
        self.name = name
        self.age =age
        self.lastname = lastname
        self.salary = salary

    def showInfo(self):
        print(f'Employee ID: {self.id} \n Name: {self.name} {self.lastname} \n Age: {self.age} \n Salary: {self.salary} \n')
       
while True:
    id  = int(input('Enter employee ID: '))
    name = input('Enter employee name: ')
    lastname = input('Enter employee lastname: ')
    age = int(input('Enter employee age: '))
    salary = float(input('Enter employee salary: ')) 
    print("do you want to register your employee or not? (y/n): ")



employee1 = Employee(id,name,lastname,age,salary)


employee1.showInfo()




