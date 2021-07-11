usersList = {
    "John": "1234",
    "George": "2345",
    "Paul": "3456",
    "Ringo": "4567"
}
def nameCheck():
    for key in usersList:
        givenName = input(print("Enter your name: "))
        if givenName == usersList[key]:
            return True
        else:
            return False

def psswrdCheck():
    for value in usersList:
        givenPsswrd = input(print("Enter your password: "))
        if givenPsswrd == usersList[value]:
            return True
        else:
            return False

def main():
    if nameCheck() is True:
        psswrdCheck()
    elif nameCheck() is True and psswrdCheck() is True:
        print("You're logged in'")
    elif nameCheck() is True and psswrdCheck() is False:
        print("Correct name but password is wrong")
    else:
        print("Wrong name")
                
if __name__ == '__main__':
    main()