#)The program must prompt the user for a username and password. The program should 
#compare the password given by the user to a known password. If the password matches, the 
#program should display “Welcome!” If it doesn’t match, the program should display “I don’t 
#know you
def Login():
    Username= input("Enter your Username: ")
    Password= input("Enter your Password: ")
    if Password=="abc$123" or Password=="ABC$123":
        print("WELCOME!!",Username)
    else:
        print("I don't know you")

Login()
