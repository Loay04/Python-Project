people={}
def add():
    id=input("Enter the contact ID: ")
    name=input("Plaese type a name: ")
    phone_number=int(input("Please type a number: "))
    people["ID"] = id
    people["name"] = name
    people["number"] = phone_number
    print(f"{name} was added successfully..")
def view():
    print(people)
def edit():
    id=input("Enter the contact ID: ")
    name=input("Plaese type a name: ")
    phone_number=int(input("Please type a number: "))
    people["ID"] = id    
    people["name"] = name
    people["number"] = phone_number
while True:
    print("Contact Mangment")
    print("1- Add a contact")
    print("2- View contact")
    print("3- Edit a contact")
    print("4- Exit")

    choice = input("Please choose a number from 1-4:")
    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        edit()
    elif choice == "4":
        break
    else:
        print("Invalid input.....")