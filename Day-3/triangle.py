"""
 Check if its a valid triangle or not if yes print the area
 Area=hb/2

 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/23/2019
 Time: 8:17 PM
 """
import math

x = float(input("Enter triangle value x : "))
y = float(input("Enter triangle value y : "))
z = float(input("Enter triangle value z : "))

if x + y > z and x + z > y and y + z > x:
    s = (x + y + z) / 2
    area = math.sqrt(s * (s - x) * (s - y) * (s - z))
    print("Triangle Area = " + str(area))
else:
    print("Triangle could not be formed with given value.".title())
