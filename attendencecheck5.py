attendence=[1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1]
days_present=sum(attendence)
print(f"attendence is {days_present} out of 30")
if days_present<28:
    print("perfect attendence")
else:
    print("attendence falls below 75%")
