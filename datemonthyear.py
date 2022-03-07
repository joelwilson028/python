months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]

date = input("Enter date in MMDDYYYY format: ")
monthIndex = int(date[:2]) - 1
month = months[monthIndex]
day = date[2:4]
year = date[4:]

newdate = month + ' ' + day + ', ' + year
print(newdate)