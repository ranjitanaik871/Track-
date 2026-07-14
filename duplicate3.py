#inventory duplicate finder
#duplicate product code
product_code=["c21","b32","j32","b21","c21","b32","t21","t21"]

#take from user, from product code
code=input("enter the product code:")
#using count ,how many times repeted 
print("count:",product_code.count(code))

#checks the condition
if code in product_code:
   print("the first occurance of product code",product_code.index(code))
else:
   print("product code not found")
