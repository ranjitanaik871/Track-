#location with latitude and longitude
loc1=(3,5)
loc2=(4,2)
loc3=(0,2)
#printing all location
list=[loc1,loc2,loc3]
print("location list",list)

print("location 1:",loc1[0],loc1[1])
print("location 2:",loc2[0],loc2[1])
print("location 3:",loc3[0],loc3[1])

try :
    loc2[0]=10
except TypeError as a:
    print(a)




