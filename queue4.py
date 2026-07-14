#Task assignment queue
#pending task
tasks=["paper writing","reading","mailing","meeting","managing"]
print("Task:",tasks)
print(' '*20)
#uses pop to assign next task(from the front of queue)
assigned=tasks.pop(3)
print("assigned:",assigned)
print("remaining tasks in queue:",tasks)
print(' '*20)
#added new task
new_task=["database","backuping","email"]
print("New task:",new_task)
#display with new and all added task
tasks.extend(new_task)
print(tasks)
