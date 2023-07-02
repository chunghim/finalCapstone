# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

############ Menu Fucntions ################

# Register a new user 
def reg_user():

    user_exist = True
    
    while user_exist:
        # - Request input of a new username
        new_username = input("New Username: ")
        # Check if the new username exists as a present key in the dictionary
        if new_username in username_password:
            print("Username already exists, please try again with a different username.")

        else:
            # Set to false to exit the loop
            user_exist = False
            # - Request input of a new password
            new_password = input("New Password: ")

            # - Request input of password confirmation.
            confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
            if new_password == confirm_password:
                # - If they are the same, add them to the user.txt file,
                print("New user added")
                username_password[new_username] = new_password

                with open("user.txt", "w") as out_file:
                        user_data = []
                        for k in username_password:
                            user_data.append(f"{k};{username_password[k]}")
                        out_file.write("\n".join(user_data))

            else:
                print("Passwords do no match")    

# Adding a task
def add_task():

    # While loop so that the user enters a valid username. Original code would just continue and display invalid username 
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
    
        else:
            break
            
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
    Include 'No' to indicate if the task is complete.'''
    new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

# View all tasks
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
    '''
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


# View tasks assigned to user
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''
    # Added a tasks_assigned boolean to display to user if no tasks are assigned to them
    tasks_assigned = False
    disp_str = ""
    # using enumerate to iterate over task_list while being able to keep track of the index, this then used to display task number
    for i, t in enumerate(task_list):
        if t['username'] == curr_user:
            disp_str += f"\nTask {i + 1}\n" # +1 so the task numbers are more meaningful, instead of starting 0
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            # To show completion station of task
            disp_str += f"Task Complete?: {'Yes' if t['completed'] else 'No'}\n"
            print(disp_str)    
            tasks_assigned = True
            disp_str = ""  # Reset disp_str for the next task
            # Add a separator line if there are more tasks
            if i < len(task_list) - 1:
                print("----------------------------------------")
    
    # If no tasks are assigned to the user, display appropriate message
    if not tasks_assigned:
        print("\nThere are no tasks assigned to you")
        return
    
    task_index = -1

    while True:
        
        # Try-except to validate that a user enters a number to select a task
        try: 
            task_selection = int(input("Select a task number to Mark as Complete, Edit or Enter -1 to return to main menu: "))

            if task_selection == -1: # Returns the user to the main menu
                return
                    
            if task_selection <= 0 or task_selection > i + 1: # 0 deemed invalid as task numbers start at 1. i keeps track of number of tasks, so if number is higher than i+1 than that is also deemed invalid
                print("Invalid task selected")
                break
            
            else:
                task_index = task_selection -1 # Adjusting for the + 1 when displaying task numbers to make them more readable 


            chosen_task = task_list[task_index]

            # Check to see if the task is already marked as complete, if so no editing / further action is allowed and returns the user to the main menu.
            if chosen_task['completed']:
                print("The Task chosen has already been marked as complete")
                return

            # Prompt the user to choose to either mark as complete or edit task
            task_action = input("Enter 'c' to mark task as complete or 'e' to edit chosen task: ").lower()

            if task_action == 'c':
                # Mark the task as complete
                chosen_task['completed'] = True
                with open("tasks.txt", "w") as task_file:
                    task_list_to_write = []
                    # Rewrite the task with updated attribute of complete
                    for t in task_list:
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                            "Yes" if t['completed'] else "No"
                        ]
                        #split by semi colon and then joined and written to file
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))
                print("Task marked as complete.")
                return
            
            elif task_action == 'e':
                # Prompt user to edit due date or assignee
                task_edit = input("Enter 'd' to change due date or 'a' to change assignee: ").lower()

                if task_edit == 'd':
                    new_due_date = input("Enter a new due date in the format YYYY-MM-DD: ")

                    try:
                        # Converting a string representation of time into a date time object
                        chosen_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                        
                        with open("tasks.txt", "w") as task_file:
                            task_list_to_write = []
                            # Rewrite the task with updated due_date attribute
                            for t in task_list:
                                str_attrs = [
                                    t['username'],
                                    t['title'],
                                    t['description'],
                                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                    "Yes" if t['completed'] else "No"
                                ]
                                task_list_to_write.append(";".join(str_attrs))
                            task_file.write("\n".join(task_list_to_write))
                        print("Due date has been updated")
                    
                    # Handle invalid date formats
                    except ValueError:
                        print("Invalid date format entered, please try again with YYYY-MM-DD")
                    
                    return
        
                elif task_action == 'a':
                    # Changing the assigned user of a task to a new user. 
                    new_assignee = input("Please enter the new assignee for this task: ")
                    chosen_task['username'] = new_assignee

                    with open("task.txt", "w") as task_file:
                        task_list_to_write = []
                        # Rewrite the task with updated username attribute
                        for t in task_list:
                            str_attrs = [
                                t['username'],
                                t['title'],
                                t['description'],
                                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                                "Yes" if t['completed'] else "No"
                            ]
                            task_list_to_write.append(";".join(str_attrs))
                        task_file.write("\n".join(task_list_to_write))
                    print("New user has been assigned this task")
                    return

                else:
                    print("Invalid option. Please try again.")
                    return       
        # Handle incorrect input when user is meant to be selecting a task to perform action on.
        except ValueError:
            print("Invalid input, please try again and enter a task number")

def generate_reports():
    # Calculating values for task_overview.txt
    total_tasks = len(task_list) 
    completed_tasks = sum(task['completed'] for task in task_list) # Sums up the number of tasks that completed is true iterating through each task in task_list
    uncompleted_tasks = total_tasks - completed_tasks # using the total number of tasks to subtract the number of completed tasks
    overdue_tasks = sum(not task['completed'] and task['due_date'] < datetime.today() for task in task_list) # Sum the number of tasks complete false, and the due_date is beyond todays current date. 
    uncomplete_percentage = (uncompleted_tasks / total_tasks) * 100 # multiplication to work out percentage
    overdue_percentage = (overdue_tasks / uncompleted_tasks) * 100 # multiplacation to work out percentage

    # Format report output into user-friendly easy to read.
    task_report = f'''
    Total tasks: {total_tasks}
    Completed tasks: {completed_tasks}
    Uncompleted tasks: {uncompleted_tasks}
    Overdue tasks: {overdue_tasks}
    Uncomplete as %: {uncomplete_percentage}%
    OVerdue as %: {overdue_percentage}%
    '''
    # print(task_report)

    # Write task overview report to file
    with open('task_overview.txt', 'w') as task_file:
        task_file.write(task_report)

        print("task_overview.txt successfully generated")

    # Calculate total number of users registered
    total_users = len(username_password)
    user_report = f'''User Overview:
Total users: {total_users}
Total tasks: {total_tasks}
\n
'''
    # Iterate over username_passwword to access each username to then check the name against a task
    for user in username_password.keys():
        
        # Initialise variables with counts set to 0
        user_tasks = 0
        user_complete = 0
        user_incomplete = 0
        user_overdue = 0

        # Go through each task and matching the task username to the user from username_password
        for task in task_list:

            if task['username'] == user: # Matched task increase count by 1
                user_tasks += 1

                if task['completed']: # Completed task increase count by 1
                    user_complete += 1
                
                else:
                    user_incomplete += 1 # If it's not completed, then it's uncompleted, increase count by 1

                    if task['due_date'] < datetime.today(): # Check if due_date is less than current date, if not then it's overdue and increase count by 1
                        user_overdue += 1

        # Avoiding division by zero errors, if division values are not greater than zero, set the result as 0
        user_task_percentage = (user_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        user_completed_percentage = (user_complete / user_tasks) * 100 if user_tasks > 0 else 0
        user_incomplete_percentage = (user_incomplete / user_tasks) * 100 if user_tasks > 0 else 0
        user_overdue_percentage = (user_overdue / user_tasks ) * 100 if user_tasks > 0 else 0
        # 
        user_report += f'''User: {user}
Total number of tasks assigned: {user_tasks}
Number of tasks assigned as %: {user_task_percentage}%
Tasks assigned completed as %: {user_completed_percentage}%
Uncomplete tasks assigned as %: {user_incomplete_percentage}%
Overdue tasks as %: {user_overdue_percentage}%
\n
''' 
    # Write user report to file
    with open('user_overview.txt', 'w') as user_file:
        user_file.write(user_report)      
        
        print("user_overview.txt successfully generated")

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True
        # Add boolean flag here to set True if admin user has logged in
        is_admin = (curr_user == 'admin')


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    # Adjusted additional menu options to show when admin user is logged on using is_admin boolean
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
''' + ('gr - Generate reports\n' if is_admin else '') + ('ds - Display statistics\n' if is_admin else '') + # Only shown if admin user is logged in.
'e - Exit: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
       
    elif menu == 'vm':
        view_mine()
    
    elif menu == 'gr' and curr_user == 'admin':
        generate_reports()
                
    
    elif menu == 'ds' and curr_user == 'admin': 

        # Variables to store file names for task and user
        task_report_file = "task_overview.txt"
        user_overview_file = "user_overview.txt"

        # Check if either report is available, if not, generate reports function will be called
        if not os.path.exists(task_report_file) or not os.path.exists(user_overview_file):
            generate_reports()
        
        # open task overview read only, then print the contents
        with open(task_report_file, 'r') as task_file:
            task_report = task_file.read()
            print(task_report)

        # open user report as read only, then print the contents
        with open(user_overview_file, 'r') as user_file:
            user_report = user_file.read()
            print(user_report)


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")