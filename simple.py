def loan_eligibility(credit,salary):
  if(credit>=720):
   if(salary>30000):
     print("eleigible")
   else:
     print("salary is low")
  else:
     print("credit score is low")
loan_eligibility(250,25000)