# Payroll Processing Function
def process_payroll(employee_dict):
    net_salary = {}

    for name, salary in employee_dict.items():
        hra = salary * 0.10
        deduction = salary * 0.05
        net = salary + hra - deduction
        net_salary[name] = net

    return net_salary


employees = {
    "Ravi": 30000,
    "Priya": 40000,
    "Amit": 35000
}

result = process_payroll(employees)

print("Payroll Details")
for name, salary in result.items():
    print(name, ":", salary)