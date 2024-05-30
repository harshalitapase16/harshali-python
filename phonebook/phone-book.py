phonebook = {}

while True:

 print( """
 1. Add contact
 2. Delete contact
 3. Search contact
 4. View all contact
 5. Exit
 """)
 usr_inp = input("Enter your choice: ")
 if usr_inp == '1':
  name = input("Enter name: ")
  phone = input("Enter Phone number: ")
  if name not in phonebook:
    phonebook[name] = phone
    print("Your contact is saved!")
  else:
   print("Name is already exist..")
  
 elif usr_inp == '2':
  name = input("Enter name: ")
  if name in phonebook:
   del phonebook[name]
   print("Deleted Successfully!")
  else:
   print("This is not found!")

 elif usr_inp == '3':
  name = input("Enter name: ")
  if name in phonebook:
   ph = phonebook[name]
   print(f"Name is {name} and Number is {ph}")
  else:
   print("Not found!")
 
 elif usr_inp == '4':
  for k,v in phonebook.items():
   print(f"{k} : {v}")
 
 elif usr_inp == '5':
  break
 
 else:
  print("You Entered wrong number")