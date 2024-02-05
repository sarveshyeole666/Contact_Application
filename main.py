class contact:
    def __init__(self,name,mob,mail=None):
        self.name = name
        self.mob = mob
        self.mail = mail

class app:
    def __init__(self):
        self.contacts = []

    def add_contact(self,name,mob,mail):
        self.contacts.append(contact(name,mob,mail))

    def search_(self,name):
        for c in self.contacts:
            if c.name == name:
                return f'mob = {c.mob} mail = {c.mail}'
        return None

    def del_contact(self,name):
        for c in self.contacts:
            if c.name == name:
                self.contacts.remove(c)
                return
        return ValueError('Contact doesnt exist')

    def display_all(self):
        for c in self.contacts:
            print(f'name = {c.name} mob = {c.mob} mail = {c.mail}')

    def update_mob(self,name,mob):
        for c in self.contacts:
            if c.name == name:
                c.mob = mob
                return

    def update_mail(self,name,mail):
        for c in self.contacts:
            if c.name == name:
                c.mail = mail
                return

    def update_name(self,old,new):
        for c in self.contacts:
            if c.name == old:
                c.name = new
                return




