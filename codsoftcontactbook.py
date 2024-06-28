contact={}
#function to add a new contact
def add_contact():
    name=input("Enter name: ")
    phone=input("Enter phone number: ")
    email=input("Enter email: ")
    address =input("Enter address: ")
    contact[name]={"phone":phone,"email":email,"address":address}
    print("Contact added successfully")
    #view contact
def view_contact():
    print("Contact List:")
    for name,details in contact.items():
        print(f"Name:{name}, Phone: {details['phone']}")
    #search contact
def search_contact():
    query=input("Enter name or phone number to search: ")
    for name, details in contact.items():
     if query in name or query in details['phone']:
       print(f"Name:{name},Phone:{details['phone']},Email:{details['email']},Address:{details['address']}")
       return
    print("Contact not found")
    #uodate contact
def update_contact():
  name =input("Enter name of contact to update: ")
  if name in contact:
    phone=input("Enter new phone number: ")
    email=input("Enter new email: ")
    address=input("Enter new address: ")
    contact[name]={"phone":phone,"email":email,"address":address}
    print("Contact updated successfully")
  else:
    print("Contact not found")
    #delete contact
def delete_contact():
    name=input("enter name of contact to delete: ")
    if name in contact:
      del contact[name]
      print("contact deleted successfully")
    else:
      print("Contact not found")
    #main program
while True:
  print("Contact Manangement Program")
  print("1.Add Contact")
  print("2.View Contact")
  print("3.Search Contact")
  print("4.Update Contact")
  print("5.Delete Contact")
  print("6.Quit")
  choice=input("Enter your choice: ")
  if choice=="1":
    add_contact()
  elif choice=="2":
     view_contact()
  elif choice=="3":
     search_contact()
  elif choice=="4":
     update_contact()
  elif choice=="5":
     delete_contact()
  elif choice=="6":
     break
  else:
    print("Invalid choice")
add_contact()
view_contact()
search_contact()
update_contact()
delete_contact()
