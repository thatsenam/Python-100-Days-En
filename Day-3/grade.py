"""
CGPA result system
80 points ~ 100 points，print -> A+
75 points ~ 79 points，print -> A
70 points ~ 74 points，print -> A-
65 points ~ 69 points，print -> B+
60 points ~ 64 points，print -> B
55 points ~ 59 points，print -> B-
50 points ~ 55 points，print -> C+
45 points ~ 49 points，print -> C
40 points ~ 44 points，print -> D
below 40 points, print->F

 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/21/2019
 Time: 10:24 AM
 
 """

point = int(input("Enter your point(limit:0 ~ 100)  : "))
if 100 >= point >= 80:
    grade = 'A+'
elif 79 >= point >= 75:
    grade = 'A'
elif 74 >= point >= 70:
    grade = 'A-'
elif 69 >= point >= 65:
    grade = 'B+'
elif 64 >= point >= 60:
    grade = 'B'
elif 59 >= point >= 55:
    grade = 'B-'
elif 54 >= point >= 50:
    grade = 'C+'
elif 50 >= point >= 45:
    grade = 'C'
elif 44 >= point >= 40:
    grade = 'D'
elif point < 40:
    grade = 'F'
else:
    print('Invalid point.')
print("Your cgpa/grade is : " + grade)
