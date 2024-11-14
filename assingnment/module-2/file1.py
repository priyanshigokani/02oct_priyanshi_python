new=open("new.txt","w")

id =input("Enter your id: ")
name=input("Enter your name: ")
city=input("Enter your city: ")

new.write(f"id:{id}\nname:{name}\ncity:{city}")