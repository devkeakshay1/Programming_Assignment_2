### 3. Write a Python program to display calendar?
##### Sol.


import calendar
year=int(input("Enter year : "))
month=int(input("Enter month : "))

#It is module in python.
#This is only for month calender for perticular year and month
Month_Calendar=calendar.month(year,month)
print("The calender for month is :")
print(Month_Calendar)

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




#This is only for year 2022
import calendar
year1=int(input("Enter year1 : "))
Year_Calendar=calendar.calendar(year1)
print("The calender for year is :")
print(Year_Calendar)


######################################
#########ANSWER################

#            Enter year1 : 2022
#            The calender for year is :
#                                            2022
#
#                January                   February                   March
#            Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                            1  2          1  2  3  4  5  6          1  2  3  4  5  6
#            3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
#            10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
#            17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
#            24 25 26 27 28 29 30      28                        28 29 30 31
#            31
#
#                April                      May                       June
#            Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                        1  2  3                         1             1  2  3  4  5
#            4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
#            11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
#            18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
#            25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
#                                    30 31
#
#                    July                     August                  September
#            Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#                        1  2  3       1  2  3  4  5  6  7                1  2  3  4
#            4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
#            11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
#            18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
#            25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30
#
#                October                   November                  December
#            Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 #                           1  2          1  2  3  4  5  6                1  2  3  4
 #           3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
 #           10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
 #           17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
#
