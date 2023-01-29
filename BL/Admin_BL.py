from BL.Person import person


class Admin(person):

    def __init__(self, name=None, id=None, password=None, designation=None):
        super().__init__(name, id, password, designation)
