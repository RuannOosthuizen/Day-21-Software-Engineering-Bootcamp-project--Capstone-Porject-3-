#=====importing libraries===========
# Here I am importing the current date at any time.
# Reference : https://www.programiz.com/python-programming/datetime/current-datetime#
# Reference: https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import date
from datetime import datetime

first_login = True

#=====Functions Section=====#
# Function for user to login:
def login():
    user_pass = False
    pass_pass = False

    # Here the while loop, loops untill the user enters their credentails correctly
    while not user_pass:
        login_name = input("To login please enter your username:\t")

        # This for loop checks to see if the username inputted is stored in the "user.txt" file.
        for x in range(0, len(users_details)):
            if users_details[x][0] == login_name:
                user_pass = True

                # If the username exists then the user can enter their password which is also checked to see if its correctly entered.
                if user_pass:
                    while not pass_pass:
                        login_password = input("Please enter your password\t")
                        if users_details[x][1] == login_password:
                            pass_pass = True

                        # If the password doesnt match the user is prompted to try again.
                        if not pass_pass:
                            print("Password is incorrect. Please try again.")

            # If the username does not exist the user is prompted to try a different username.
            if not user_pass:
                print("Username is incorrect. Please try again.")
            
        print(f"Login succefful! Welcom {login_name}")
    return login_name


# Function for new user detailse to be added.
def reg_user():
        print("\nRegistering a New User:")
        unique_username = False
        verify_pass = False

        # Here the if statement checks to see if the user is "admin" if not the suer logged in isnt given access to register a new user.
        if username == "admin":
            print("To register a new user please enter the details below.\n")

            # This while loop, loops untill the admin enters a new username that doestn exist already.
            while not unique_username:
                unique = True
                new_user = input("Please enter the new users name:\t")

                # This for loop then checks to see if the username already exists or not.
                for x in range(0, len(users_details)):
                    if users_details[x][0] == new_user:
                        print("This username already registered. Please try again.")
                        unique = False
                    if unique:
                        unique_username = True

            # This while loop then loops to checks for the user to confirm the new password.
            while not verify_pass:
                new_password1 = input("Please enter the password for this user:\t")
                new_password2 = input("Please confirm the password:\t")

                # If the passwords match the new users details is then written in the "user.txt" file
                if new_password1 == new_password2:
                    verify_pass = True
                    with open("user.txt", "a+") as user_file:
                        user_file.write(f"\n{new_user}, {new_password1}")
                        user_file.close()
                        print(f"\nThe new user has been added\nUsername:\t{new_user}\nPassword:\t{new_password1}")

                # If the password does not match the admin can try again.
                else:
                    print("The password does not match. Please try again.")

            verify_pass = False

        # If the user logged in is not the admin.
        else:
            print("You are not authorside to register a new user.\nPlease select a different option.")


# Function to add a new task to the "tasks.txt" file.
def add_task():
    print("\nAdding a New Task:")
    print("To add a new task please enter all the details below:")

    # These variabels are defined to store the input from the user.
    info = []
    info_format = ["Username assigned to this task:\t", "Task Title:\t", "Task Description:\t", "Due Date (e.g. 15 Sep 2020):\t"]
    # Here the current date is imported.
    today = date.today()
    current_date = today.strftime("%d %b %Y")

    # These loops then loop for each input and stores it in a list.
    for x in range(0, 4):
        while True:
            data = input(f"{info_format[x]}")

            # This if statment makes sure the user doesnt enter a empty input.
            if data == "":
                print("Invalid input. Please try again.")
            else:
                info.append(data)
                break
    
    # Inserting the "No" for completion and the current date for assigned date.
    info.insert(6, "No")
    info.insert(4, current_date)

    # Here the new task is then written to the "tasks.txt" file in the correct format.
    with open("tasks.txt", "a+") as tasks_file:
        tasks_file.write(f"\n{info[0]}, {info[1]}, {info[2]}, {info[3]}, {info[4]}, {info[5]}")
        tasks_file.close()
        print("The new task has been added to the 'tasks.txt' file.")


# Function to view all the tasks stored in "tasks.txt" file.
def view_all():
    print("\nView All Tasks:")

    # Here the for loop, loops through the "tasks_details" list and prints it to the user is a easy to ready format.
    for line in tasks_details:
        print("----------------------------------------------------")
        print(f'''
Task:               {line[1]}
Assigned to:       {line[0]}
Date assigned:     {line[3]}
Due date:           {line[4]}
Task Complete?      {line[5]}
Task description:\n {line[2]}\n''')
        print("----------------------------------------------------")


# Function to view, mark and edit only the tasks assigned to the user logged in.
def view_mine():
    print("\nView My Tasks:")
    user_found = False
    my_tasks = []

    # This for loop, loops throuhg the task list and adds the task relating to 
    # the user who is currently logged in to the "my_tasks" variable.
    for x in range(0, len(tasks_details)):
        if username == tasks_details[x][0]:
            my_tasks.append(tasks_details[x])
            user_found = True

    # If the "user_found" equals "True" all the tasks assigned to them is then printed in a easy to read format.
    # as well as labelling each task with a number.
    if user_found:

        for x in range(0, len(my_tasks)):
            print(f"\nTask {x + 1}")
            print("----------------------------------------------------")
            print(f'''
Task:               {my_tasks[x][1]}
Assigned to:       {my_tasks[x][0]}
Date assigned:     {my_tasks[x][3]}
Due date:           {my_tasks[x][4]}
Task Complete?      {my_tasks[x][5]}
Task description:\n {my_tasks[x][2]}\n''')
            print("----------------------------------------------------")

        # Here the user is then prompted to mark or edit the task they select or leave to the menu.
        while True:

            # Here a try block is used for incase the user input is incorrectly inputted.
            try:
                task_num = int(input("Please select a task you wish to mark or edit by typing in the number that corresponds to the task.\nIf you wish to leave to the menu enter -1:\t"))
                # If the user wants to leave to the menu.
                if task_num == -1:
                    break
                
                # If the user has selected a task.
                elif task_num > 0 and task_num <= len(my_tasks):
                    # This for loop then removes that selected task to mark or edit then add the newly
                    # marked or edited task back to the lsit.
                    for x in range(0, len(my_tasks)):
                        tasks_details.remove(my_tasks[x])
                    while True:
                        # The user is able to pick to mark or edit the selected task.
                        user_choice = input("Please select to mark or edit the selected task.\n'm' to mark or 'e' to edit:\t")
                        
                        # Here the if statement then either marks the task as completed by changing the "No" to "Yes".
                        # Or letting the user edit the user assigned to the task or due date of the task if the task is not already marked as complete.
                        if user_choice == "m":
                            my_tasks[task_num - 1][5] = "Yes"
                            print(f"\nTask {task_num} has been marked as complete.")
                            break

                        elif user_choice == "e":
                            if my_tasks[task_num - 1][5] == "Yes":
                                print("\n This task has been marked as completed and cant be editted.")
                                break
                            
                            else:
                                print("\nPlease enter the new user assigned to the task and new due date of the task.\nLeave blank if no changes are required.")
                                usern = input("New Username:\t")
                                new_due_date = input("New due date for this task:\t")

                                if usern != "":
                                    my_tasks[task_num - 1][0] = usern
                                if new_due_date != "":
                                    my_tasks[task_num - 1][4] = new_due_date

                                print("Task details have been updated.")
                                break

                        # If the user wished to leave to the menu.
                        elif user_choice == "-1":
                            break

                        # If the user input is not recognised.
                        else:
                            print("Unrecognised input. Please try again.")

                    # Here the newly edited task is then added to the list
                    # using the "seek" and "truncate" functions.
                    # and then written to the task file.
                    with open("tasks.txt", "w") as tasks_file:
                        for x in range(0, len(my_tasks)):
                            tasks_details.append(my_tasks[x])
                        for x in range(0, len(tasks_details)):
                            tasks_file.write(", ".join(tasks_details[x]))
                            if x != len(tasks_details) - 1:
                                tasks_file.write("\n")
                        tasks_file.close()
                    break
                
                # If the user enters a number that doesnt exists.
                else:
                    print("The selected task does not exist. Please try again.")

            except:
                print("No task number enterd. Please try again.")

    # If there are no tasks assigned to the user they are then informed about this.
    if not user_found:
        print("No tasks are currently assaigned to you.")


# Function to display statistics to the admin user.
def display_statistics():

    # Here the if statement checks to see if the user is "admin" if not the user logged in isnt given access to view the statistics.
    if username == "admin":

        # Here the function to generate reporst is called incase the ifnromation has changed.
        generate_reports()

        # Here the report files are opnened and read.
        task_over = open("task_overview.txt", "r")
        user_over = open("user_overview.txt", "r")

        # Due to the difference in the way the terminal and text documents
        # deal with the Tab (\t) delimter, the format needs to be adjusted
        # for the information being read from the files and printed to screen.
        # Here we are removing all \t delimters from the file, and adding new
        # \t delimiters based on the needs of the terminal.
        for line in task_over:
            if "Total" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))

            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))
        
        for line in user_over:
            if "User:" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t\t"))

            elif "User Tasks" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))

            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))

    # If the user logged in isnt the admin they dont have access to the statistics.
    else:
        print("\nYou are not authorised to view statistics.\n")

# Function to generate the reports of the tasks and userse.
def generate_reports():

    # Here the if statement checks to see if the user is "admin" if not the user logged in isnt given access to generate the reports.
    if username == "admin":

        # Here the files are opend and created if they dont exist yet.
        task_over_write = open("task_overview.txt", "w+")
        user_over_write = open("user_overview.txt", "w+")
        
        # Here are the variables defined that will be used to track and store the data.
        total_tasks = len(tasks_details)
        num_completed = 0
        num_incomplete = 0
        num_inc_overdue = 0
        per_incomplete = 0
        per_overdue = 0

        #=====Task_Overview.txt File=====#

        # Here the for loop, loops through the "task_overview" data and updates the appropriate variables.
        for x in range(0, len(tasks_details)):

            if tasks_details[x][5] == "Yes":
                num_completed += 1

            elif tasks_details[x][5] == "No":
                num_completed += 1

                # Here the overdue tasks are calculated.
                int_date = tasks_details[x][4].split()

                # Here the string is the seperated and casted to integers.
                day = int(int_date[0])
                year = int(int_date[2])
                # A month dictionary with number values is set to enable calculation of string month into an integer. 
                months_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul':7, 'Aug': 8, 'Sep':  9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
                # Then formated correctly.
                month = months_dict[int_date[1][0: 3]]

                # Correctly formatting the current date:
                date_now = date.today().strftime('%d %b %Y')

                # The same process is repeated for the current date.
                date_now_list = date_now.split()
                day_2 = int(date_now_list[0])
                year_2 = int(date_now_list[2])
                month_2 = months_dict[date_now_list[1]]

                date_task = (year + month + day)
                date_now = (year_2 + month_2 + day_2)

                # Then the if statements check to se if its over due or not.
                if date_task > date_now or date_task == date_now:
                #task_date = datetime.strptime(tasks_details[x][4], '%d %b %Y')
                #print(task_date)
                #if datetime.date(datetime.now()) < task_date.date():
                    num_inc_overdue += 1

        # If the number of tasks are zero we dont want to devide by zero so i set the variables to zero then.
        if total_tasks == 0:
            per_incomplete = 0
            per_overdue = 0

        else:
            per_incomplete = round(100 * num_incomplete / total_tasks)
            per_overdue = round(100 * num_inc_overdue / total_tasks)

        # Then the statistics is written to the text file.
        task_over_write.write("Task Overview - Statistics relating to all tasks in task_manager.py\n\n")
        task_over_write.write(f"Total Tasks:\t\t{total_tasks}\nCompleted Tasks:\t{num_completed}\nIncomplete Tasks:\t{num_incomplete}\nOverdue Tasks:\t\t{num_inc_overdue}\nPortion Incomplete:\t{per_incomplete}%\nPortion Overdue:\t{per_overdue}%")

        #=====User_Overview.txt File=====#

        # The "user_overview" text file is then written to.
        num_users = len(users_details)
        user_over_write.write("User Overview - Statistics relating to all users in task_manager.py\n\n")
        user_over_write.write(f"Total Users:\t\t{num_users}\n")
        user_over_write.write(f"Total Tasks:\t\t{total_tasks}")

        # The is repeated for each user in the variable:
        for x in range(0, len(users_details)):
            num_tasks = 0
            num_completed = 0
            num_incomplete = 0
            num_inc_overdue = 0
            per_incomplete = 0
            per_overdue = 0
            per_completed = 0
            por_tasks = 0

            user_over_write.write("\n----------------------------------------------------\n")
            user_over_write.write(f"User:\t\t\t\t\t{users_details[x][0]}\n")

            # Here the for loop, Loops through each task.
            for y in range(0, len(tasks_details)):

                # Check if the task is assigned to the current user we are looping.
                # Update the variables based on the info from every task (similar to above)
                if users_details[x][0] == tasks_details[y][0]:
                    num_tasks +=1

                    if tasks_details[y][5] == "Yes":
                        num_completed += 1

                    elif tasks_details[y][5] == "No":
                        num_incomplete += 1

                        # Here the overdue tasks are calculated.
                        int_date = tasks_details[x][4].split()

                        # Here the string is the seperated and casted to integers.
                        day = int(int_date[0])
                        year = int(int_date[2])
                        # A month dictionary with number values is set to enable calculation of string month into an integer. 
                        months_dict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul':7, 'Aug': 8, 'Sep':  9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
                        # Then formated correctly.
                        month = months_dict[int_date[1][0: 3]]

                        # Correctly formatting the current date:
                        date_now = date.today().strftime('%d %b %Y')

                        # The same process is repeated for the current date.
                        date_now_list = date_now.split()
                        day_2 = int(date_now_list[0])
                        year_2 = int(date_now_list[2])
                        month_2 = months_dict[date_now_list[1]]

                        date_task = (year + month + day)
                        date_now = (year_2 + month_2 + day_2)

                        # Then the if statements check to se if its over due or not.
                        if date_task > date_now or date_task == date_now:
                        #task_date = datetime.strptime(tasks_details[x][4], '%d %b %Y')
                        #print(task_date)
                        #if datetime.date(datetime.now()) < task_date.date():
                            num_inc_overdue += 1

            # If the number of tasks are zero we dont want to devide by zero so i set the variables to zero then.
            if num_tasks == 0:
                per_incomplete = 0
                per_overdue = 0
                per_completed = 0

            else:
                per_incomplete = round(100 * num_incomplete / num_tasks)
                per_overdue = round(100 * num_inc_overdue / num_tasks)
                per_completed = round(100 * num_completed / num_tasks)

            if total_tasks == 0:
                por_tasks = 0

            else:
                por_tasks = round(100 * num_tasks / total_tasks)

            # Write the statistics calculated above to the file.
            user_over_write.write(f"User Tasks:\t\t\t\t{num_tasks}\nPortion Total Tasks:\t{por_tasks}%\nPortion Completed:\t\t{per_completed}%\nPortion Incomplete:\t\t{per_incomplete}%\nPortion Overdue:\t\t{per_overdue}%")
            user_over_write.write("\n----------------------------------------------------\n")
        
        # Close the files
        print("Reports have been generated: task_overview.txt, user_overview.txt")
        task_over_write.close()
        user_over_write.close()

    # If the current user is not the "admin" they are not authorised to use the function
    else:
        print("You are not authorised to generate reports.")


#=====Login and Menu Selection Section=====#

while True:
    # Here the "user.txt" and "tasks.txt" files are read and stored in variables to be used later on.
    with open("user.txt", "r+") as user_file:
        users_details = user_file.readlines()
        users_details = [x.strip().split(", ") for x in users_details]

    with open("tasks.txt", "r+") as tasks_file:
        tasks_details = tasks_file.readlines()
        tasks_details = [x.strip().split(", ") for x in tasks_details]

    # Here the user is prompted the login section where they can then input their username and password.
    if first_login:
        username = login()
        first_login = False

    # Here the menu printed is determined by either the username being admin or just a normal user.
    # The menu is different depnding on is the user logged in is the admin or not.
    if username == "admin":
        menu = input("""Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
\n""").lower()
    
    else:
        menu = input("""Please select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
\n""").lower()

    # Then with the user input the appropriate functions are called.
    # If the user wants to register a new user.
    if menu == "r":
        reg_user()

    # If the user wants ot add a new task.
    elif menu == "a":
        add_task()

    # If the user wants to view all the tasks.
    elif menu == "va":
        view_all()

    # If the user wants to view all the tasks assigned to them only.
    elif menu == "vm":
       view_mine()

    # If the user wants to view the overview of users and tasks.
    elif menu == "gr":
        generate_reports()
    
    # If the user wants to view a report.
    elif menu == 'ds':
        display_statistics()

    # If the user wants to logout they can so by pressing "e":
    elif menu == "e":
        print("\nYou have successfully been logged out.")
        break

    # If the user types in the incorrect selection they will be informed and will be given the menu again.
    else:
        print("You have made a wrong choice, Please Try again")

    user_file.close()
    tasks_file.close()