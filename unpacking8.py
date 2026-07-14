#employee data from database
emp=(125,"ravi","Manager",50000)

emp_id,name,department,salary=emp

#printing values
#using unpacking method

print(emp_id)
print(name)
print(department)
print(salary)
print(' '*20)
 
print(f"{'Employee_ID'}{' '*5}{'Name'}{' '*5}{'Department'}{' '*5}{'Salary'}")      
print(f"{125}{' '*13}{"ravi"}{' '*6}{"Manager"}{' '*6}{50000:.2f}")