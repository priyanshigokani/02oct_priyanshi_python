#Write a Python program to show hierarchical inheritance
class Parents:
    def get_data(self):
        print("This is parents class!")

class Daughters(Parents):
    def get_data1(self):
        print("This is daughters class!!!")

class Son(Parents):
    def get_data2(self):
        print("This is son's class!!!")

obj1=Son()
obj1.get_data()
obj1.get_data2()

obj2=Daughters()
obj2.get_data()
obj2.get_data1()