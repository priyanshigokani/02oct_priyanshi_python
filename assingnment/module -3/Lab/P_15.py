#  Write a Python program to show multiple inheritance.
class ava:
    a_id=0
    a_std=""

    def v_getdata(self):
        self.a_id=input("Enter ava's ID: ")
        self.a_std=input("Enter ava's Study: ")

class jules:
    j_id=0
    j_std=""

    def j_getdata(self):
        self.j_id=input("Enter jules's ID: ")
        self.j_std=input("Enter Jules's Study: ")

class ana:
    an_id=0
    an_std=""

    def p_getdata(self):
        self.an_id=input("Enter ana's ID: ")
        self.an_std=input("Enter ana's Study: ")

class chen(ava,jules,ana):
    def printdata(self):
        print("-------------ava's Data------------")
        print("ava's ID: ",self.a_id)
        print("ava's Study: ",self.a_std)
        print("-------------jules's Data------------")
        print("Jules's ID:",self.j_id)
        print("Jules's Study:",self.j_std)
        print("-------------ana's Data------------")
        print("ana's ID: ",self.an_id)
        print("ana's Study: ",self.an_std)

c=chen()
c.v_getdata()
c.j_getdata()
c.p_getdata()
c.printdata()