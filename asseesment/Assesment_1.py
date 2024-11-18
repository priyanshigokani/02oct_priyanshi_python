#E_notebook

import datetime 

def add_note():
    title=input("Enter your title of the note: ")
    description=input("Enter your note description: ")
    name = get_valid_name()

    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    try:
        with open("notes.txt","a") as file:
            file.write(f"{timestamp}\n")
            file.write(f"e-note title: {title}\n")
            file.write(f"e-note description: {description}\n")
            file.write(f"note generator: {name}\n\n")
            print("Notes added successfully!")

            log_transaction("Generated note:")
    except Exception as e:
        print(f"Error: {e}")


def get_valid_name():
    while True:
        name = input("Enter your name: ")
        
        if  all(c.isalpha() or c.isspace() for c in name):
            return name
        else:
            print("Invalid input")


def view_notes():
    try:
        print("\n your notes: ")
        with open("notes.txt", "r") as file:
            notes = file.read()

            if notes:
                print(notes)
            else: 
                print("no notes available")

            log_transaction("View all notes")
    except Exception as e: 
        print("an error occurred while viewing notes:")

def log_transaction(action):
     timestamp = datetime.datetime.now().strftime("%d %m %Y  %I:%M:%S %p %A")
     with open("log.text", "a") as log_file:
         log_file.write(f"{timestamp} - {action}\n")

def display_menu():
    print("\n    E-notebook Application     ")
    print("1. for generate note")
    print("2. for view note")
    print("3. for Exit")

def main():
    while True:
        display_menu()

        try: 
            choice = input("Enter your choice: "). strip()

            if choice == '1':
                add_note()
                print("Your notes added successfully!")
            elif choice == '2':
                view_notes()
            elif choice == '3':
                print("Exiting the application. Thank you!")
                log_transaction("Exited the application")
                break
            else:
                print("Invalid choice. please enter 1,2,or 3")
        except Exception as e:
            print("An unexpected error occurred: ", e)

main()





