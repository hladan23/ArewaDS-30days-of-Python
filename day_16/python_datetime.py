# Exercises: Day 16

from datetime import datetime
# Q1 Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now)                     
day = now.day                  
month = now.month               
year = now.year                 
hour = now.hour                
minute = now.minute             
second = now.second
timestamp = now.timestamp()  # 2023-12-19 10:08:22.549883

# Q2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
d = now.strftime("%m/%d/%Y, %H:%M:%S")
print(d) #12/19/2023, 10:08:22


# Q3 Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object) #2019-12-05 00:00:00


# Q4 Calculate the time difference between now and new year.
t_day = date(2023,12,19)
new_year = date(2024,1,1)
time_to_new_year = new_year - t_day
print(f'Time to new year is {time_to_new_year} ') #Time to new year is 21 days, 0:00:00 


# Q5 Calculate the time difference between 1 January 1970 and now.
# I've assigned the current year,month and day from above
print(date(year,month,day) - date(1970,1,1)) #19702 days      

# Q6 Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
# The datetime module is a versatile tool that plays a crucial role in a wide range of applications, providing a standardized way to work with dates and times in Python.