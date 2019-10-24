"""
Find out the number of all daffodils between 100 and 999
The number of daffodils is the number of cubes and equal to the number itself.
Such as: 153 = 1**3 + 5**3 + 3**3
153 is daffodil number
370 is daffodil number
371 is daffodil number
407 is daffodil number


 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/24/2019
 Time: 10:29 PM
 """

for i in range(100, 1000):
    last = i % 10
    second_last = i // 10 % 10
    third_last = i // 10 // 10
    if last ** 3 + second_last ** 3 + third_last ** 3 == i:
        print(f"{i} is daffodil number")
