# Task Priority Sorter
#task provided with priority number
tasks = ["Project Report", "Testing", "Meeting", "Documentation"]
priorities = [1, 2, 4, 3]

#using if-elif-else and give the condition with their priority
for i in range(len(tasks)):
    if priorities[i] == 1:
        label = "Urgent"
    elif priorities[i] == 2 or priorities[i] == 3:
        label = "Normal"
    else:
        label = "Low"

    print(tasks[i], "-", label) 