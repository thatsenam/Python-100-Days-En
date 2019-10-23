"""
 # ---- Find prime number ----
 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/23/2019
 Time: 10:02 PM
 """
import math

number = int(input("Enter a number : "))
square_root = int(math.sqrt(number))
is_prime = True
for i in range(1, square_root + 1):
    if number % i == 0:
        is_prime = False
        break
if number != 1 and is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")