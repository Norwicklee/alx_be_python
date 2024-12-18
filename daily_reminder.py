task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")
match priority:
    case "high":
        reminder = f"Task: {task} - Priority: High"
    case "medium":
        reminder = f"Task: {task} - Priority: Medium"
    case "low":
        reminder = f"Task: {task} -Priority: Low"
    case _ :
        reminder = f"Task: {task} - Priority: Unknown"

# Modify the reminder if the task is time-bound
if time_bound == 'yes':
    reminder += " - This task requires immediate attention today!"

# Provide a customized reminder
print(reminder)
