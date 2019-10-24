"""
 playing with for loop

 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/23/2019
 Time: 8:59 PM
 """

# ---- summation of  1 to 101 ----
import math

sum = 0
for i in range(1, 101):  # step is 1
    sum += i
print(f"1 +to 101 = {sum}")

# ---- summation of  2 to 101 with step 2 ----
sum = 0
for i in range(2, 101, 2):  # step is 2
    sum += i
print(f"2 +to 101 with step 2 = {sum}")

# ---- Enter a non-negative integer n to calculate n! ----

n = 3  # int(input("Enter the value of n : "))
result = 1

for i in range(1, n + 1):
    result *= i
print(f"n! = {result}")

# Enter two positive integers to calculate the greatest common divisor and the least common multiple

a = 5
b = 9
for factor in range(a, 0, -1):
    print("in loop : ", factor)
    if a % factor and b % factor:
        print(f"{a},{b} is divisible by {factor}")
        print(f"The least common multiple {a},{b} is  {(a * b) // factor}")
