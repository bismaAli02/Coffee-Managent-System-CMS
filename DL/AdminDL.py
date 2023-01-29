from BL.Admin_BL import Admin
from UI.personUI import personUI
from BL.Person import person


class AdminDL:
    Admin = []

    @staticmethod
    def AddIntoList(user):
        AdminDL.Admin.append(user)

    @staticmethod
    def deleteAdmin(id):
        i = 0
        for user in AdminDL.Admin:
            if user.id == id:
                AdminDL.Admin.pop(i)
            i = i+1

    @staticmethod
    def updateAdmin(id):
        j = 0
        for i in AdminDL.Admin:
            if(i.id == id):
                user = personUI.addUser()
                AdminDL.Admin[j] = user
                break
            j = j+1

    @staticmethod
    def viewAdmins():
        print("Name    Id    Password    Designation")
        print(" ")
        i = 0
        for user in AdminDL.Admin:
            print(user.name, " ", user.id, " ",
                  user.password, " ", user.designation)

    @staticmethod
    def CheckAdmin(id, password):
        for user in AdminDL.Admin:
            if(user.id == id and user.password == password):
                return True
