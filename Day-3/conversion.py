"""
 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/21/2019
 Time: 9:58 AM
 Problem : Convert inches to centimeter and centimeter to inches
 Formula : multiply the length value by 2.54 to get centimeter
 """

length = float(input("Enter Length : "))
length_unit = input("Enter Unit (eg. cm,centimeter,in,inches) : ")
if length_unit == 'in' or length_unit == 'inches':
    print(f"{length} inches = {length * 2.54} centimeter")
elif length_unit == 'cm' or length_unit == 'centimeter':
    print(f"{length} centimeter = {length / 2.54} inches")
else:
    print("invalid length")
