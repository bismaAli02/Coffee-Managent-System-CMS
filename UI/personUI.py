from BL.Admin_BL import Admin


class personUI:

    @ staticmethod
    def addUser():
        name = input("Enter a name: ")
        id = input("Enter a id: ")
        password = input("Enter a Password: ")
        designation = input("Enter a designaton: ")
        user = Admin(name, id, password, designation)
        return user

    @ staticmethod
    def userID():
        id = input("Enter id of user: ")
        return id
