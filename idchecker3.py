#duplicate emp_id checker
emp_id=[101,202,301,301,204,201,101,405,205]
#useing len ,it takes the id length
x=len(emp_id)
print("original_id")
print(emp_id)
#make one separate unique id using set() to remove duplicate
unique=set(emp_id)
#checks the length of duplicate value
y=len(unique)
print("unique id")
print(unique)
#duplicate removed from original id ,stores in z variable
z=x-y
print("Duplicate ids count")
print(z)