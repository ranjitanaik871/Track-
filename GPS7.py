#GPS location logger
#fixed longitude,latitude of delivery stops
delivery=[(77.9176,88.216),(89.7169,12.1412),(916.823,816.234)]

#accessing individual latitude/longitude using index
for i in range(len(delivery)):
    print("stop",i+1,":",delivery[i])