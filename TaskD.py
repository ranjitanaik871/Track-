tasks=["paper writing","reading","mailing","meeting","managing"]
print("Task:",tasks)
print(' '*20)

assigned=tasks.pop(3)
print("assigned:",assigned)
print("remaining tasks in queue:",tasks)
print(' '*20)

new_task=["database","backuping","email"]
print("New task:",new_task)

tasks.extend(new_task)
print(tasks)
