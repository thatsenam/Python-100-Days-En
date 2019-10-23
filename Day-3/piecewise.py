"""
 Solve the following functions

        3x - 5  (x > 1)
 f(x) = x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)

 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/22/2019
 Time: 5:16 PM
 """

x = float(input("Enter the value of F(x): "))
y = 0
if x > 1:
    y = 3 * x - 5
elif -1 <= x <= 1:
    y = x + 2
elif x < -1:
    y = 5 * x + 3
print("f(%.2f) is equal to %.2f" % (x, y))
