"""
 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/19/2019
 Time: 10:18 PM
 Code : Find leap year.
 What is leap year?
 A leap year is a year in which an extra day is added to the Gregorian calendar, which is used by most of the
 world. While an ordinary year has 365 days, a leap year has 366 days. ... A leap year comes once every four
 years. Because of this, a leap year can always be evenly divided by four.
 """
year = int(input("Enter a year (eg. 2015): "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Woh woh! its a leap year")
else:
    print("ops ! its not a leap year")
