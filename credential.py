class Credentials:
    creden_list = []
    def __init__(self, account, user_name, pass_word):
        self.account = account
        self.user_name = user_name
        self.pass_word = pass_word
    def saveCred(self):
        Credentials.creden_list.append(self)
    @classmethod
    def displayCredentials(cls):
        return cls.creden_list

# class Credentials:
#     # Add+Save new credentials
    
#     Credential_list = []
    
# def __init__(self, account, username, password):
#         self.account = account
#         self.username = username
#         self.password = password

# def saveCred(self):
#         Credentials.credential_list.append(self)

# def displayCredentials(cls):
#         return cls.credential_list