import time
import datetime



class Task:
    def __init__(self, title, description, s_date, e_date):
        self.title = title
        self.description = description
        self.s_date = s_date
        self.e_date = e_date
        self.complete = False
        
class ParentTask(Task):
    def __init__(self, title, description, s_date, e_date, subtasks):
        super().__init__(title, description, s_date, e_date)
        self.subtasks = subtasks


tasks = []

def add_task():
    try:
        print("\nAdd a task")

        is_subtask = input("\nIs this a subtask? (y/n): ")

        if is_subtask.lower() == 'y':
            parent_identifier = input("\nEnter the index or title of the parent task: ")
            parent_task = None
            
            try:
                # Try to interpret parent_identifier as an integer index
                parent_index = int(parent_identifier)
                parent_task = tasks[parent_index]
                
                
            except ValueError:
                # If parent_identifier can't be interpreted as an integer, assume it's a title
                for task in tasks:
                    if task.title == parent_identifier:
                        parent_task = task
                        break
            
            if parent_task is None:
                raise ValueError("Invalid parent identifier.")
            
            title = input("\nEnter name of subtask: ")
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

            s_date_unix = int(s_date_converted.timestamp())
            e_date_unix = int(e_date_converted.timestamp())

            subtask = Task(title, descrip, s_date_unix, e_date_unix)
            parent_task.subtasks.append(subtask)
            print("\nSubtask added successfully!")
        else:
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

            s_date_unix = int(s_date_converted.timestamp())
            e_date_unix = int(e_date_converted.timestamp())

            task = ParentTask(title, descrip, s_date_unix, e_date_unix, [])
            tasks.append(task)
            print("\nTask added successfully!")
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

        if isinstance(task, ParentTask):
            print("Parent Task")
            print(f"""{i} : {task.title}\n
            {task.description}\n
            {'Complete' if task.complete else 'Incomplete'}\n
            Time remaining: {time_remaining_str}""")

            if task.subtasks:

                for j, subtask in enumerate(task.subtasks):
                    # calculate the time remaining until the end date
                    time_remaining = subtask.e_date - int(time.time())

                    # Calculate the time remaining in months, days, and minutes
                    seconds_remaining = max(0, time_remaining)
                    minutes_remaining, seconds_remaining = divmod(seconds_remaining, 60)
                    hours_remaining, minutes_remaining = divmod(minutes_remaining, 60)
                    days_remaining, hours_remaining = divmod(hours_remaining, 24)
                    months_remaining, days_remaining = divmod(days_remaining, 30)

                    # Format the time remaining as a string
                    time_remaining_str = f"{months_remaining} months, {days_remaining} days, {hours_remaining} hours, {minutes_remaining} minutes"

                    print(f"""\t{j} SubTask : {subtask.title}\n
                    {subtask.description}\n
                    {'Complete' if subtask.complete else 'Incomplete'}\n
                    Time remaining: {time_remaining_str}""")
        else:
            print(f"""{i} : {task.title}\n
            {task.description}\n
            {'Complete' if task.complete else 'Incomplete'}\n
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


def handle_choice(choice):
    functions = [add_task, view_task, edit_task, edit_title, edit_description, mark_done, unmark_done, remove_task]
    
    if choice.isdigit() and 1 <= int(choice) <= len(functions):
        functions[int(choice) - 1]()
    else:
        print("Invalid choice.")
# Main loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Edit a task")
    print("4. Edit the title of a task")
    print("5. Edit the description of a task")
    print("6. Mark a task as done")
    print("7. Unmark a task as done")
    print("8. Remove a task")
    print("9. Exit")
    choice = input("Enter an option: ")
    if choice == '9':
        break
    
    handle_choice(choice)
    



