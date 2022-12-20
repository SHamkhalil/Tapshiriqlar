import datetime 

d = int(input("Day: ")) 
m = int(input("Month: ")) 
y = int(input("Year: "))  

date = datetime.date(y, m, d)  

nextdate = date + datetime.timedelta(days=1)  

print(f"Sabahsi gun:  {nextdate.day} {nextdate.month} {nextdate.year}")