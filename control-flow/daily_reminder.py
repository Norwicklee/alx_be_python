task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
 #Ask if the task is time-bound
time_bound = input("Is the task time-bound? (yes/no): ").lower()
#Process task based on Priority and Time
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
