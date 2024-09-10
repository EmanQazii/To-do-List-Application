import csv
import os
from tabulate import tabulate
def valid_date(d_str):
    from datetime import datetime
    try:
        date=datetime.strptime(d_str,"%Y-%m-%d").date()
        today=datetime.today().date()
        if date>=today:
            return True
        else:
            print("The date must be of day or in future")
            return False
    except ValueError:
        print("The date must be in format 'yyyy-mm-dd'")
        return False

def add_task():
    while True:
        num_task=input("How many task do you want to add(max 10 at a time)?:")
        if num_task.isdigit():
            num_task=int(num_task)
            if 0 <= num_task <=10:
                break
            else:
                print("Enter the number in tha range 1 to 10")
        else:
            print("Invalid Entry..Try again!")
    
    for t in range(num_task):
        print("Enter the details of task # ", t+1," : ")
        task=input("Enter the task description : ")
        print("Select priority of the task")
        while True:     
            s=int(input("Enter '1' for HIGH, '2' for MEDIUM, '3' for LOW : "))
            if s==1:
                priority='High'
                break
            elif s==2:
                priority='Medium'
                break
            elif s==3:
                priority='Low'
                break
            else:
                print('Invalid entry..Select options from 1 to 3.')
        while True:        
            due_date=input("Enter the due date (yyyy-mm-dd) : ")
            if valid_date(due_date):
                break
        with open ('task.csv','a',newline='') as file:
            writer=csv.writer(file)
            writer.writerow([task,priority,due_date])
    print("Tasks added successfully!!")

def view_tasks():
    try:
        with open('task.csv','r') as file:
            reader=csv.reader(file)
            row= list(reader)
            headers=["Task Description","Priority","Due Date"]
            print(tabulate(row,headers=headers,tablefmt='grid'))
    except FileNotFoundError:
        print("Error!!File not found!!")

def delete_task():
    try:
        with open('task.csv','r') as file:
            reader= csv.reader(file)
            tasks=list(reader)
    except FileNotFoundError:
        print('File not found!!')
        return
    for index,task in enumerate(tasks):
        print(index+1," : ",task)
    while True:
        id=input("Enter the index of one of the above tasks to be removed : ")
        if id.isdigit():
            id=int(id)
            id-=1
            if 0<= id <= len(tasks):
                d_task=tasks.pop(id)
                with open('task.csv','w',newline="") as file:
                    write=csv.writer(file)
                    write.writerows(tasks)
                print("The task # ", id+1,' : ',d_task ,'is deleted successfully!')
                break
            else:
                print("Error! Enter the id from the above given list")
        else:
            print("Invalid Task Number Entered!")

def update_task():
    try:
        with open('task.csv','r') as file:
            reader= csv.reader(file)
            tasks=list(reader)
    except FileNotFoundError:
        print('File not found!!')
        return
    for index,task in enumerate(tasks):
        print(index+1," : ",task)
    while True:
        id=input("Enter the index of one of the above tasks you want to update : ")
        if id.isdigit():
            id=int(id)
            id-=1
            if 0<= id <= len(tasks):
                cur_task=tasks[id]
                n_task=input(f"Enter the new description(or press enter to not update the previous description : '{cur_task[0]}'): ")
                print("Select priority of the task")
                while True:     
                    s=input(f"Enter '1' for HIGH, '2' for MEDIUM, '3' for LOW (or press enter to not update the previous description : '{cur_task[1]}'):")
                    if s=='1':
                        n_priority='High'
                        break
                    elif s=='2':
                        n_priority='Medium'
                        break
                    elif s=='3':
                        n_priority='Low'
                        break
                    elif s=='':
                        n_priority=cur_task[1]
                        break
                    else:
                        print('Invalid entry..Select options from 1 to 3.')
                while True:        
                    n_date=input(f"Enter the due date (yyyy-mm-dd) (or press enter to not update the previous description : '{cur_task[2]}'): ")
                    if n_date=='':
                        n_date =cur_task[2] 
                        break
                    elif valid_date(n_date):
                        break
                tasks[id]=[
                    n_task if n_task else cur_task[0],
                    n_priority,
                    n_date ]
                
                with open('task.csv','w',newline='') as file:
                    write=csv.writer(file)
                    write.writerows(tasks)
                print("The task with index # ",index+1," is updated successfully!")
                break
            else:
                print("Error! Enter the id from the above given list")
        else:
            print("Invalid Task Number Entered!")

def search_task():
    while True:
        print("1. Search by priority \n2. Search by Date")
        op=input('Select one option : ')
        if op.isdigit():
            op=int(op)
            if op==1:
                os.system("cls")
                search_by_priority()
                break
            elif op==2:
                os.system("cls")
                search_by_date()
                break
            else:
                print("Select an option between 1 and 2")
        else:
            print("Error!Enter a valid option!")

def search_by_priority():
    try:
        with open('task.csv','r') as file:
            read=csv.reader(file)
            tasks=list(read)
    except FileNotFoundError:
        print('File not Found!')
        return
    print("Select priority of the task")
    while True:     
        s=int(input("Enter '1' for HIGH, '2' for MEDIUM, '3' for LOW : "))
        if s==1:
            priority='High'
            break
        elif s==2:
            priority='Medium'
            break
        elif s==3:
            priority='Low'
            break
        else:
            print('Invalid entry..Select options from 1 to 3.')
    
    print(f"Tasks with the priority : '{priority}' are as follows:")
    found=False
    for idx,task in enumerate(tasks):
        if task[1]==priority:
            found=True
            print(idx+1," : ",task)  
    if not found:
        print(f"The tasks with priority : '{priority}' does not exist")

def search_by_date():
    try:
        with open('task.csv','r') as file:
            read=csv.reader(file)
            tasks=list(read)
    except FileNotFoundError:
        print('File not Found!')
        return
    while True:        
        due_date=input("Enter the due date (yyyy-mm-dd) : ")
        if valid_date(due_date):
            break
    print(f"Tasks with the due date : '{due_date}' are as follows:")
    found=False
    for idx,task in enumerate(tasks):
        if task[2]==due_date:
            found=True
            print(idx+1," : ",task)  
    if not found:
        print(f"The tasks with due date: '{due_date}' does not exist")
