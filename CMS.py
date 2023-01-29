from DL.EmployeeDL import EmployeeDL
from UI.personUI import personUI
from BL.Person import person
from DL.AdminDL import AdminDL
from UI.MenuUI import MenuUI


def main():

    while(True):
        id, password = MenuUI.LoginPortal()
        if(id == "123@" and password == "asd"):
            while(True):
                Option = MenuUI.ownerMenu()
                if Option == "1":
                    user = personUI.addUser()
                    AdminDL.AddIntoList(user)
                elif Option == "2":
                    id1 = personUI.userID()
                    AdminDL.deleteAdmin(id1)
                elif Option == "3":
                    id2 = personUI.userID()
                    AdminDL.updateAdmin(id2)
                elif Option == "4":
                    AdminDL.viewAdmins()
                elif Option == "5":
                    break
                else:
                    print("You entered wrong option: ")

        elif(AdminDL.CheckAdmin(id, password) and person.designation == "Admin"):
            while(True):
                Option = MenuUI.AdminMenu()
                if Option == "1":
                    user = personUI.addUser()
                    EmployeeDL.AddIntoList(user)
                elif Option == "2":
                    id1 = personUI.userID()
                    EmployeeDL.deleteEmployee(id1)
                elif Option == "3":
                    id2 = personUI.userID()
                    EmployeeDL.updateEmployee(id2)
                elif Option == "4":
                    EmployeeDL.viewAllEmployee()
                elif Option == "5":
                    break
                else:
                    print("You entered wrong option: ")
        elif(person.designation == "Employee"):
            empty = ""
        else:
            print("You entered wrong option: ")


if __name__ == "__main__":
    main()
