#employee boarding checklist
#task issued in the list
task=["laptop issued","id card issued","email issued"]
print("list of task:",task)

#use append to add the new task
task.append("compliance training")
print("new task:",task)

#using insert(), can add the urgent task using index
new=task.insert(0,"writing")
print("urgent task:",task)