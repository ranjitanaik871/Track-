#monthly report extract
#12 months revenue figure
monthly_revenue=[10000,50000,23000,45000,45250,89000,75000,12300,14000,10000,25000,35000]
print("Monthly  Revenue:",monthly_revenue)
#uses slicing to extract only first quarter(month 1-3)
first_quarter=monthly_revenue[1:3]

print("first quarter:",first_quarter)
#uses slicing to extract the last quarter(month 10-12)
last_quarter=monthly_revenue[10:12]
print("Last quarter:",last_quarter)

#uses concatenation to combine both quarters
peak_season=first_quarter+last_quarter
print("Peak season:",peak_season)