from app_functions import *
import os
def menu():
    print("MY TASK APPLICATION")
    print("-------MAIN MENU---------")
    print("1- Add task")
    print("2- View all tasks")
    print("3- Delete task")
    print("4- Search a specific task")
    print("5- Update task")
    print("6- Exit")
    
def main():
    while True:
        os.system("cls")
        menu()
        op=input('Select an option : ')
        if op.isdigit():
            op=int(op)
            if op==1:
                os.system("cls")
                add_task()
            elif op==2:
                os.system("cls")
                view_tasks()
            elif op==3:
                os.system("cls")
                delete_task()
            elif op==4:
                os.system("cls")
                search_task()
            elif op==5:
                os.system("cls")
                update_task()
            elif op==6:
                exit(0)
        else:
            print("Invalid Entry!!You entered an invalid option!")
        n=input("Do you want to return to main menu ? (y/n) : ")
        if n.lower()!='y':
            break
if __name__=='__main__':
    main()
