# Prompt user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task using Match Case and conditional logic
match priority:
    case "high":
        reminder = f"'{task}' is a high-priority task."
    case "medium":
        reminder = f"'{task}' is a medium-priority task."
    case "low":
        reminder = f"'{task}' is a low-priority task."
    case _:
        reminder = f"'{task}' has an undefined priority level. Please clarify its importance."

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Display the reminder
print("\nReminder:")
print(reminder)