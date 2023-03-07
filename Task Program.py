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


add_task()
view_task()




