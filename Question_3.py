### 3. Write a Python program to display calendar?
##### Sol.


import calendar
year=int(input("Enter year : "))
month=int(input("Enter month : "))

#It is module in python.
calendar=calendar.month(year,month)

print(calendar)

##############################################
##########ANSWER##############

#            Enter year : 2021
#            Enter month : 12
#            December 2021
#            Mo Tu We Th Fr Sa Su
#                1  2  3  4  5
#            6  7  8  9 10 11 12
#            13 14 15 16 17 18 19
#            20 21 22 23 24 25 26
#            27 28 29 30 31