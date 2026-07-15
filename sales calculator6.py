#sales total calculator(function)

def calculate_total(sales):
    #compute total,average
    total = sum(sales)
    average = total / len(sales)
    #return both values
    return total, average
#sample list of 7 days of sales
sales = [100, 200, 150, 300, 250, 400, 350]

total, average = calculate_total(sales)
#print the results
print("Total:", total)
print("Average:", average)