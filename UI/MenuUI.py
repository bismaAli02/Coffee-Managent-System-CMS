class MenuUI:
    @ staticmethod
    def ownerMenu():
        print("//////////////  Main Menu ///////////////")
        print(" ")
        print("1-  Add new Admin")
        print("2-  Delete Admin")
        print("3-  Update Admins")
        print("4-  View All Admins")
        Option = input("Enter your choice: ")
        return Option

    @staticmethod
    def LoginPortal():
        print("///////// Login Portal ////////")
        print(" ")
        print("Enter your login information: ")
        id = input("Enter your id: ")
        password = input("Enter your password: ")
        return id, password

    def AdminMenu():
        print("//////////////  Main Menu ///////////////")
        print(" ")
        print("1-  Add new Employee")
        print("2-  Delete Employeee")
        print("3-  Update Employee")
        print("4-  View All Employee")
        print("5-  Add new Product")
        print("6-  Delete Product")
        print("7-  Update Product")
        print("8-  View All  Products")
        print("9-  View products under specific price")
        print("10- View drinks Menu")
        print("11- View food Menu")
        print("12- View Monthly sale of each employee")
        print("13-  View Products less than minimum quantity")

        Option = input("Enter your choice: ")
        return Option

    @staticmethod
    def statusMenu():
        print("Select your Status:  >")
        print("a.... Owner")
        print("b.... Admin")
        print("c.... Employee")
        print("d.... Exit")
        status = input("Choose your option: ")
        return status
