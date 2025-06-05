task = input("Enter your task: ")  #Accept task description
priority = input("Priority (high/medium/low): ").lower()  #Accept priority
time_bound = input("Is it time-bound? (yes/no): ").lower()  #Accept time-bound status

#Check: Match case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Task: '{task}' has unknown priority"

#Check: Add message for time sensitivity
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if "Note:" not in reminder:
        reminder += ". Consider completing it when possible."

#Check: Final reminder output
print(reminder)