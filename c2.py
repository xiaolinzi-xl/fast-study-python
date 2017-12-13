# coding=utf-8
class User():
    type = "User"

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def __repr__(self):
        return self.id + " " + self.name

class Admin(User):
    type = "Admin"

    def __init__(self,id,name,group):
        User.__init__(self,id,name)
        self.group = group

    def __repr__(self):
        return self.id + " " + self.name + " " + self.group

if __name__ == '__main__':
    admin = User('1','xioalinzi')
    print admin