from BL.Employee_BL import Employee
from UI.personUI import personUI


class EmployeeDL:
    Employee = []

    @staticmethod
    def AddIntoList(user):
        EmployeeDL.Employee.append(user)

    @staticmethod
    def deleteEmployee(id):
        i = 0
        for user in EmployeeDL.Employee:
            if user.id == id:
                EmployeeDL.Employee.pop(i)
            i = i+1

    @staticmethod
    def updateEmployee(id):
        j = 0
        for i in EmployeeDL.Employee:
            if(i.id == id):
                user = personUI.addUser()
                EmployeeDL.Employee[j] = user
                break
            j = j+1

    @staticmethod
    def viewEmployee():
        print("Name    Id    Password    Designation")
        print(" ")
        i = 0
        for user in EmployeeDL.Employee:
            print(user.name, " ", user.id, " ",
                  user.password, " ", user.designation)
