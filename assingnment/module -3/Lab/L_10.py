#Write Python programs to demonstrate method overloading and method overriding

#method overloading
class stud_info:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)
    
    def getdata(self,sal):
        print("Salary:",sal)

st=stud_info()
st.getdata(101,'ava')
st.getdata(457.34)


#method overriding
class Parent:
    def getdata(self):
        print("Hello from parent's class")
	
class Child(Parent):
    def getdata(self):
        print("Hello from child's class")

c=Child()
c.getdata()
p=Parent()
p.getdata()
