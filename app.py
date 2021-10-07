from Userclass import User
from Credentialsclass import Credentials
from random import randint
'''for the user class'''
def createUser(username, password):
    myUser = User(username, password)
    return myUser
def saveUser(user):
    user.saveUser()
def displayUsers():
    User.displayUsers()
    '''this is for the credentials class'''
def createCredentials(account, username, password):
    myCred = Credentials(account, username, password)
    return myCred

def saveCredentials(credentials):
    credentials.saveCred()
def displayCredentials():
    return Credentials.displayCredentials()
    
def main():
    print("Welcome to the Pass volt,")
    print("\n")
    while True: 
        shortcodes= input("Do the following,type; nu -to create user account , du -to display user , ex -to exit:").lower()
        if shortcodes == "nu":
            username = input("Enter your username:")
            password = input("Enter your password:")
            saveUser(createUser(username, password))
            print(f"Hello {username} your pass volt account has successfully been created")
            print("\n")

            while True:
                print("Welcome {username} to the section of adding accounts and their passwords:")
                print("-"*20)
                code =input("To proceed, choose the following to interact with the application:  nc -to create credentials: dc -to display credentials:").lower()
                if code == "nc":
                    feedback = input("Enter y to create your own password and n for the system to generate:").lower()
                    if feedback == ("y"):
                        account = input("Enter the name of account, eg facebook, instagram, twitter:")
                        user_name = input("Enter your desired username:")
                        pass_word = input("Enter the password:")
                        saveCredentials(createCredentials(account,username, password))
                        print("Credentials successfully uploaded")
                    elif feedback == "n":
                        account = input("Enter the name of account, eg facebook, instagram, twitter:")
                        user_name = input("Enter your desired username:")
                        pass_word = randint(123456789,987456321)
                        saveCredentials(createCredentials(account, username, password))
                        print(f"Hello {user_name} Your password is {pass_word}......SAVED!!!")    
                    else:
                        print("We didnt what you really want!!!")
                elif code == "dc":
                    if displayCredentials():

                        for credential in displayCredentials():
                            print(f"Account: {credential.account} Username:{credential.user_name} Password:{credential.pass_word}")
                    else:
                        print("No accounts to display")
                else:   print("Sorry,could not process what you want")
                # if code == "ex":
                        # print("Exit successful")
         # below for the parent
        elif shortcodes == "du":
            for user in User.users:
                print(f"{user.username}")
        elif shortcodes == "ex":
            print("Exit successful")
            break
        else: print("Kindly check your entry again")   
main()