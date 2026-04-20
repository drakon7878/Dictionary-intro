#also called data hiding

class Admin():
    def __init__(self, username , password):
        self.username = username
        self.__password = password

    def login(self):
        passInput = input("Type your password here-->")
        if passInput == self.__password:
            print("Login successful")

    def getPass(self):
        print(self.__password)


    def changePass(self):
        passInput = input("Enter your password-->")
        if passInput == self.__password:
            newPass = input("Enter the new password-->")
            self.__password = newPass
            print("Password changed")
        else:
            print("Wrong password")

admin1 = Admin("hello" , "12345")
print(admin1.username)
admin1.getPass()

admin1.changePass()
admin1.login()
