# Employee Bonus Eligibility Function

def check_bonus(years_of_experience, performance_rating):
    if years_of_experience > 2 and performance_rating >= 8:
        return "Eligible"
    else:
        return "Not Eligible"

#for printing different employees using range
for i in range(5):
    print("Employee", i + 1)

    experience = int(input("Enter years of experience: "))
    rating = int(input("Enter performance rating: "))

    result = check_bonus(experience, rating)

    print("Bonus:", result)