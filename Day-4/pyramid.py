"""
 draw pyramid using for loop

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/24/2019
 Time: 11:29 AM
 """

row = 10
for i in range(1, row):
    print("*" * i)

print()
for i in range(1, row):
    space = row - i
    for s in range(1, space):
        print(f" ", end="")
    print("*" * i)

for i in range(row):
    sibs = int(row - i)
    print(" " * sibs, end="")
    print(f"*" * (i * 2), end="")
    print(" " * sibs, end="\n")
