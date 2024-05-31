todo_list = []

usr_input = int(input("Enter how many task you want to add: "))
for num in range(1, usr_input+1):
 tasks = input(f"Enter Task {num}= ")
 if tasks not in todo_list:
  todo_list.append(tasks)
  print("Task is saved successfully...")
 else:
  print("Task is already exist!")
print(f"Total tasks are {todo_list}")

while True:
 print("""
 1. Add
 2. Update
 3. Delete
 4. View
 5. Exit
 """)
 get_inp = input("Choose any option: ")

 if get_inp == '1':
  new_task = input("Enter New task: ")
  if new_task not in todo_list:
   add_new = todo_list.append(new_task)
   print("Your task is added successfully...")
  else:
   print("Task is already exist!")

 elif get_inp == '2':
   updt_task = input("Enter task to update: ")
   if updt_task in todo_list:
    ind = todo_list.index(updt_task)
    updating_task = input("Enter the updating value: ")
    todo_list[ind] = updating_task
    print("Your task is updated successfully...")
   else:
    print("This task not exist!")

 elif get_inp == '3':
   del_inp = input("Enter task to delete it: ")
   if del_inp in todo_list:
    ind = todo_list.index(del_inp)
    del_task = todo_list[ind]
    del del_task
    print("Your task is deleted successfully...")
   else:
    print("Task is not exist in list")
 
 elif get_inp == '4':
  print(f"Total tasks are: ")
  for items in todo_list:
   print(items)

 elif get_inp == '5':
  print("Program is closed")
  break
 
 else: 
  print("Invalid Input!!!!!")