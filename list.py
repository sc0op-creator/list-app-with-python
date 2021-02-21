from os import write
import os


while True:
    user_input = input("Enter\n(a) Add a new list\n(b) Delete a list\n(c) Update a list\n--> ")
    if user_input == 'a':
        file_name = input("Enter a name for your list --> ")
        print("Press enter after adding every item and press (q) and press enter to quit ...")
        while True:
            add_items = input("--> ")
            if add_items == 'q':
                break
            else:
                with open(f"{file_name}.txt" , "a") as f:
                    f.write(f"{add_items}\n")
        break
    elif user_input == 'b':
        file_present = os.listdir('.')
        file_name = input(f"{file_present}\nWhich file do you want to remove ? --> ")
        os.remove(file_name)
        break
    elif user_input == 'c':
        file_present = os.listdir('.')
        file_name = input(f"{file_present}\nWhich file do you want to update ? --> ")
        with open(file_name,'r') as f:
            print(f.read())
        print("Press enter after adding every item and press (q) and press enter to quit ...")
        while True:
            add_items = input("--> ")
            if add_items == 'q':
                break
            else:
                with open(file_name , "a") as f:
                    f.write(f"{add_items}\n")
        break
    else:
        print('\nPlease choose a valid option...')
        
        
