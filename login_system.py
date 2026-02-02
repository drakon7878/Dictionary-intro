main_pre = {
    "user1" : "pass1",
    "user2" : "pass2",
    "user3" : "pass3",
    "user4" : "pass4",
    "user5" : "pass5",
}

main= {

}

def choice():
    print("===============")
    print(" Would you like to Sign Up and then Log In or just Log in?")
    print("Type 1 for sign up or 2 for log in")
    choiceInput = int(input("Type here -->"))
    if choiceInput == 1:
        signIn()
    elif choiceInput ==2:
        login()
    else:
        print("Please only type 1 or 2")
        choice()

def signIn():
    endNo = int(input("How many userIDs would you like to make? -->"))
    if endNo != int or endNo <= 0:
        while endNo != int and endNo <= 0:
            print("please type an integer above 0")
            endNo = int(input("How many userIDs would you like to make? -->"))

    totalNoOfPpl = 1
    print("=====Sign Up=====")
    while totalNoOfPpl <= endNo:
        username = input("Type your Username here--> ")
        password = input("Type your Password here-->")
        main[username] = password
        totalNoOfPpl +=1
    
    print("=====Log In=====")
    signUpUser = input("Type your username here -->")
    if signUpUser in main.keys():
        signUpPass = input("Type your password here -->")
        if signUpPass == main[signUpUser]:
            print("You have Signed Up and Logged In")
        else:
            passAttempts = 4
            print("Your Password is wrong. Please input it again, you have", passAttempts ,  "more attempts")
            while passAttempts > 0:
                signUpPass = input("Type your password here -->")
                if signUpPass == main[signUpUser]:
                    print("You have Signed Up and Logged In")
                    break
                else:
                    passAttempts -= 1
                    print("Your Password is wrong. Please input it again, you have", passAttempts ,  "more attempts")
            if passAttempts == 0:
                print("You have used all your attempts; please try again later")
    else:
        userAttempts = 4
        print("Your Username is wrong. Please input it again, you have", userAttempts ,  "more attempts")
        while userAttempts > 0:
            signUpUser = input("Type your username here -->")
            if signUpUser in main.keys():
                signUpPass = input("Type your password here -->")
                if signUpPass in main[signUpUser]:
                    print("You have Signed Up and Logged In")
                    break
                else:
                    passAttempts = 4
                    print("Your Password is wrong. Please input it again, you have", passAttempts ,  "more attempts")
                    while passAttempts > 0:
                        signUpPass = input("Type your password here -->")
                        if signUpPass in main[signUpUser]:
                            print("You have Signed Up and Logged In")
                            break
                        else:
                            passAttempts -= 1
                            print("Your Password is wrong. Please input it again, you have", passAttempts ,  "more attempts")
                    if passAttempts == 0:
                        print("You have used all your attempts; please try again later")             
                
            else:
                userAttempts -= 1
                print("Your Password is wrong. Please input it again, you have", userAttempts ,  "more attempts")
            if userAttempts == 0:
                print("You have used all your attempts; please try again later")

def login():
    loginUser = input("Type your username here-->")
    loginUseratps = 5
    while loginUseratps > 0:
        if loginUser in main_pre.keys():
            loginPass = input("Type your password here-->")
            loginPassAtps = 5
            while loginPassAtps > 0:
                if loginPass == main_pre[loginUser]:
                    print("You have successfully logged in")
                    return
                else:
                    print("Your passoword is wrong. You have", loginPassAtps, " more attemps")
                    loginPass = input("Type your password here-->")
                    loginPassAtps -=1
            if loginPassAtps > 4:
                print("You have used all your attemps please try again later")
                return
                    
        else:
            print("Your username is wrong. You have ", loginUseratps," more attempts" )
            loginUser = input("Type your username here-->")
            loginUseratps -=1
    if loginUseratps > 4:
        print("You have used all your attemps please try again later")
        return

choice()



