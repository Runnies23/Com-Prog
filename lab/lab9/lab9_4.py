status = True 
password = 'Python is fun'

class Login_module():
    def __init__(self):
        pass

    def Login(self):
        for index in range(1,4):
            input_password = input("Enter the password: ")
            if password == input_password:
                return True
            else: 
                print(f"Incorrect password, attempt #{index:d}")
                print("Access not allowed")
            
        return False

    def print_result(self):
        result = self.Login()
        if result:
            print("Correct password\nAccess allowed")
        else:
            print("Maximum attempts exceeded")
    
            
login = Login_module()
login.print_result()
        