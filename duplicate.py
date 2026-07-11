product_code=["c21","b32","j32","b21","c21"]
code=input("enter the product code:")
print("count:",product_code.count(code))
if code in product_code:

   print("the first occurance of product code",product_code.index(code))
else:
   print("product code not found")
