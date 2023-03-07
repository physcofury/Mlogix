import time
import datetime



class Task:
    def __init__(self, title, description, s_date, e_date):
        self.title = title
        self.description = description
        self.s_date = s_date
        self.e_date = e_date
        self.complete = False
        

tasks = []

def add_task():
    try:

        print("\nAdd a task")
        title = input("\nEnter name of task: ")
        descrip = input("\nEnter the description: ")
        while True:
            s_date = input("\nEnter the start date with the format (YYYY-MM-DD): \n")
            e_date = input("\nEnter the end date with the format (YYYY-MM-DD): \n")

            try:
                s_date_converted = datetime.datetime.strptime(s_date, "%Y-%m-%d")
                e_date_converted = datetime.datetime.strptime(e_date, "%Y-%m-%d")
                break

            except ValueError:
                print("Incorrect format. please try again")
                #time.sleep(3)

        s_date_unix = int(s_date_converted.timestamp())
        e_date_unix = int(e_date_converted.timestamp())

        task = Task(title, descrip, s_date_unix, e_date_unix)
        tasks.append(task)
    except Exception as error:
        print(error)

def view_task():
    print("\nView tasks")
    for i, task in enumerate(tasks):
        # calculate the time remaining until the end date
        time_remaining = task.e_date - int(time.time())

         # Calculate the time remaining in months, days, and minutes
        seconds_remaining = max(0, time_remaining)
        minutes_remaining, seconds_remaining = divmod(seconds_remaining, 60)
        hours_remaining, minutes_remaining = divmod(minutes_remaining, 60)
        days_remaining, hours_remaining = divmod(hours_remaining, 24)
        months_remaining, days_remaining = divmod(days_remaining, 30)


        # Format the time remaining as a string
        time_remaining_str = f"{months_remaining} months, {days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes"


        print(f"""{i} : {task.title}
        {task.description}\n\n
        {'Complete' if task.complete else 'Incomplete'}\n\n
        Time remaining: {time_remaining_str}""")

def edit_task():
    while True:
        index_or_title = input("Enter the index or title of the task: ")

        # Try to convert the input to an integer to use as an index
        try:
            index = int(index_or_title)
            task = tasks[index]
        except ValueError:
            # If the input cannot be converted to an integer, assume it is a title and search for the task by title
            for task in tasks:
                if task.title == index_or_title:
                    break
            else:
                print(f"No task with the title '{index_or_title}' found.")
                return
        
        # Ask the user which field they want to edit
        field = input("""Which field would you like to edit? Please enter a number\n
                    1: title
                    2: Description
                    3: Starting date
                    4: End date, 
                    5: Completetion status
                    0: Cancel\n """)
                    
        # Get the new value for the field from the user
        if field == "1":
            new_value = input("Enter the new title: ")

        elif field == "2":
            new_value = input("Enter the new description: ")

        elif field == "3":
            new_value = input("Enter the new start date (YYYY-MM-DD): ")

            try:
                new_value = int(datetime.strptime(new_value, '%Y-%m-%d').timestamp())

            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
            
        elif field == "4":
            new_value = input("Enter the new end date (YYYY-MM-DD): ")

            try:
                new_value = int(datetime.strptime(new_value, '%Y-%m-%d').timestamp())

            except ValueError:
                print("Incorrect format. please try again.")
                return
            
        elif field == "5":
            new_value = input("Is the task complete? (y/n): ")
            new_value = new_value.lower() == "y"

        elif field == "0":
            break

        else:
            print("Invalid field.")
            time.sleep(2)
        
         # Set the new value for the field
        num_list = ['1','2','3','4','5']
        ta_list = ['title', 'description', 's_date', 'e_date', 'complete']
        if field in num_list:
            field = int(field)
            field = ta_list[field - 1]

        print(field)
        setattr(task, field, new_value)
        print("Task updated successfully.")
        break
        
def edit_title():
    task_id = input("Enter the title or index of the task: ")
    task = None

    if task_id.isdigit():
        task = tasks[int(task_id)]
    else:
        for t in tasks:
            if t.title == task_id:
                task = t
                break
    if not task:
        print("Task not found!")
        return
    new_title = input("Enter the new title: ")
    # Validate input here
    task.title = new_title

def edit_description():
    task_id = input("Enter the title or index of the task: ")
    task = None
    if task_id.isdigit():
        task = tasks[int(task_id)]
    else:
        for t in tasks:
            if t.title == task_id:
                task = t
                break
    if not task:
        print("Task not found!")
        return
    new_description = input("Enter the new description:\n\n ")
    # Validate input here
    task.description = new_description

def mark_done():
    task_id = input("Enter the title or index of the task to mark as done: ")
    task = None
    if task_id.isdigit():
        task = tasks[int(task_id)]
    else:
        for t in tasks:
            if t.title == task_id:
                task = t
                break
    if not task:
        print("Task not found!")
        return
    task.complete = True

def unmark_done():
    task_id = input("Enter the title or index of the task to mark as incomplete: ")
    task = None
    if task_id.isdigit():
        task = tasks[int(task_id)]
    else:
        for t in tasks:
            if t.title == task_id:
                task = t
                break
    if not task:
        print("Task not found!")
        return
    task.complete = False

def remove_task():
    task_id = input("Enter the title or index of the task to remove: ")
    task = None
    if task_id.isdigit():
        task = tasks[int(task_id)]
    else:
        for t in tasks:
            if t.title == task_id:
                task = t
                break
    if not task:
        print("Task not found!")
        return
    tasks.remove(task)






