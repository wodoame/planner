from datetime import datetime, timedelta

current_date_and_time = datetime.now()
specific_date = datetime(2023, 12, 31)
# print(datetime.date(current_date_and_time)) # returns only the date part of a datetime object
print(datetime.strftime(current_date_and_time, '%d')) # formats the date with some format specifies such as %Y %d %m  and others
print(specific_date - current_date_and_time)
# print(current_date_and_time)
# print(current_date_and_time.hour, current_date_and_time.minute)
print(datetime.max)
print(datetime.today(), current_date_and_time)

print('\n\n', current_date_and_time.date() + timedelta(days=1) )