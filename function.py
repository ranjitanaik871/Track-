#conversion from celsius into fahrenheit
def convert(c):#called function
    f=(c * 9/5) + 32 
    return f #return the result

#user input
c = float(input("Enter Celsius: "))

#calling statement
print("Fahrenheit =", convert(c))