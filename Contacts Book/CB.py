contacts = {}

def add_contact(name,num):
    contacts[name] = num
    print(contacts)
    print("Add Successfully")
    
def view_contacts( ):
    if not contacts:
        print("No contacts found.")
    else:
        for name, num in contacts.items():
            print(name, num)
    
def search_contact(name):
    if name in contacts:
        print("Contact is Exist in Contact Book.")
    else:
        print("Contact is not Exist in Contact Book.")
    print(contacts)
def delete_contact(name):
    if name in contacts:
        del contacts[name]
    else:
        print("Contact Does Not Exist") 
def exit_contact():
    print("End Of The Program ")

    
print("======Contacts Book======")
print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Delete Contact")
print("5. Exit")
while True: 
    try:
        choice = int(input("Enter a Number: "))
    except ValueError:
        print("Please enter a number.")
        continue
    
    if choice == 1:
        name = input("Enter Name: ")
        num = input("Enter Contact Number: ")
        add_contact(name,num)
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        name = input("Enter Name: ")
        search_contact(name)
    elif choice == 4:
        name = input("Enter Name: ")
        delete_contact(name)
    elif choice == 5:
        exit_contact()
        break
         
    
   
