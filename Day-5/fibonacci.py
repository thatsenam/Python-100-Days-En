"""

 Output the first 20 numbers of the Fibonacci sequence
  1 1 2 3 5 8 13 21 ...
 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/24/2019
 Time: 9:42 PM
 """
n = 20
a = 0
b = 1

for i in range(n):
    # c = a + b
    # a = b
    # b = c
    a, b = b, a + b
    print(a, end=" ")
