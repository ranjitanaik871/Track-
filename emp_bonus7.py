# Employee Bonus Eligibility Function
def check_bonus(experience,rating):
    #used conditional statement
    if experience > 2 and rating >= 8:
        return "Eligible"
    else:
        return "Not Eligible"

#for printing different employees using range
for i in range(3):
    print("Employee", i + 1)

    experience = int(input("Enter years of experience: "))
    rating = int(input("Enter performance rating: "))

    result = check_bonus(experience, rating)
    print("Bonus:", result)