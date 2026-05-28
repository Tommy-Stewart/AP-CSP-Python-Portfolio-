
#Tommy
#Todo list, has a todo list that can be modified by user as they do work

#func
def todo():
    list = ['MATH', 'SPANISH', 'CHEM', 'COMPSCI', 'HUSH', 'ENGLISH']
    print("Hello! Here if your list of things to-do: ")
    print(list)
    while True:
        print(f"You have {len(list)} items on your list")
        action = input("Would you like to 1) Add an item to the list, 2) Mark an item as done, 3) Remove an item, or 4) Exit the program: ")
        if action == "":
            while True:
                add = input("What would you like to add?: ").upper().strip()
                if add == "":
                    print("Invalid input, please try again")
                else:
                    list.append(add)
                    print(list)
                    break
        elif action == "2":
            while True:
                done = input("What would you like to mark as done?: ").upper()
                try:
                    list.remove(done)
                    print(f"{list} \033[9m {done} \033[0m")
                    break
                except:
                    print("Invalid input, please try again")
        elif action == "3":
            while True:
                remove = input("What item would you like to remove?: ").upper()
                try:
                    list.remove(remove)
                    print(list)
                    break
                except:
                    print("Invalid input, please try again")
        elif action == "4":
            print("Have a great day!")
            break
        else:
            print("Invalid input, please try another answer")

#main
todo()
