# Write a Python program to show method overloading.
class stud_info:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)
    
    def getdata(self,sal):
        print("Salary:",sal)

st=stud_info()
st.getdata(101,'ava')
st.getdata(457.34)
