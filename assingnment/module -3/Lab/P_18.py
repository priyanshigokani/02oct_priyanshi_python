#Write a Python program to demonstrate the use of super() in inheritance.
class master:
    def signin(self,username,password):
        print("Username:",username)
        print("Password:",password)

class home(master):
    def signin(self,username,password):
        return super().signin(username,password)
    
class about(master):
    def signin(self,username,password):
        return super().signin(username,password)
    
a=about()
a.signin('ava',1234)

h=home()
h.signin('jules',9876)