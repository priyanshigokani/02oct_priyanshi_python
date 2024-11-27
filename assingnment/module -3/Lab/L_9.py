'''Write Python programs to demonstrate different types of inheritance 
(single, multiple, multilevel, etc.).'''
# SINGLE INHERITANCE
class Student:
    st_id=int
    st_name=str
    def get_data(self):
        self.id = input("Enter an id: ")
        self.name=input("Enter a name: ")
        print("This is Main class")

class Child(Student):
    def print_data(self):
        print("Id is: ",self.id)
        print("Name is: ",self.name)
        print("This is Sub class")
    
c=Child()
c.get_data()
c.print_data()

# MULTIPLE INHERITANCE

class GrandParent:
    def getdata(self):
        print("This Is Grandparent Class")

class Parent(GrandParent):
    def getdata1(self):
        print("This Is Parent Class")

class Child(Parent):
    def getdata2(self):
        print("This Is Child Class")

c=Child()
c.getdata()
c.getdata1()
c.getdata2()

# MULTILEVEL INHERITANCE

class ava:
    a_id=0
    a_nm=""

    def getdata(self):
        self.a_id=input("Enter ava's Id: ")
        self.a_nm=input("Enter ava's Name: ")

class jules(ava):
    jid=0
    jnm=""

    def getdata2(self):
        self.jid=input("Enter jules's Id: ")
        self.jnm=input("Enter Jules's Name: ")

class ana(jules):
    an_id=0
    an_nm=""

    def getdata3(self):
        self.an_id=input("Enter ana's Id: ")
        self.an_nm=input("Enter ana's Name: ")

class chen(ana):
    def printdata(self):
        print("-----------ava's Info--------------")
        print("ava's ID: ",self.a_id)
        print("ava's Name: ",self.a_nm)
        print("-------------Jules's Info-------------")
        print("Jules's ID: ",self.jid)
        print("Jules's Name: ",self.jnm)
        print("-------------ana's Info-------------")
        print("ana's ID:",self.an_id)
        print("ana's Name: ",self.an_nm)

k=chen()
k.getdata()
k.getdata2()
k.getdata3()
k.printdata()