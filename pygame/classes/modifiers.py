class login():
    def __init__(self, username = "" , password = ""):
        self.username = username
        self._password = password

    def getUser(self):
        print(self.username)

    def _getPassword(self):
        print(self._password)


class Admin(login):
    def __init__(self, username="", password="", role=""):
        super().__init__(username, password)
        self.role = role
    def getRoles(self):
        print("You have "+self.role+" access")


user1 = login("Jaivin", "12345")
user1.getUser()
user1._getPassword()
admin1 = Admin("admin" , "54321", "Read and write")
print(admin1.username)
print(admin1._password)
print(admin1.role)

admin1.getRoles()
admin1._getPassword()

