#Write a Python program to show multilevel inheritance. 
class ava:
    a_id=0
    a_std=""

    def a_getdata(self):
        self.v_id=input("Enter ava's ID: ")
        self.v_std=input("Enter ava's Study: ")

class Jules(ava):
    j_id=0
    j_std=""

    def j_getdata(self):
        self.j_id=input("Enter jules's ID: ")
        self.j_std=input("Enter Jules's Study: ")

class ana(Jules):
    an_id=0
    an_std=""

    def an_getdata(self):
        self.an_id=input("Enter ana's ID: ")
        self.an_std=input("Enter ana's Study: ")

class chen(ana):
    def printdata(self):
        print("-------------ava's Data------------")
        print("ava's ID: ",self.a_id)
        print("ava's Study: ",self.a_std)
        print("-------------Jukes's Data------------")
        print("Jules's ID:",self.j_id)
        print("Jules's Study:",self.j_std)
        print("-------------ana's Data------------")
        print("ana's ID: ",self.an_id)
        print("ana's Study: ",self.an_std)

c=chen()
c.a_getdata()
c.j_getdata()
c.an_getdata()
c.printdata()