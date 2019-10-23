"""
 Throwing a dice to decide what to do

 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/23/2019
 Time: 11:36 AM
 """
from random import randint

face = randint(1, 6)
if face == 1:
    print("Take breakfast")
elif face == 2:
    print("Learn Python")
elif face == 3:
    print("Learn RESTApis")
elif face == 4:
    print("Go to gym")
elif face == 5:
    print("Listen favourite song")
elif face == 6:
    print("Do whatever you want to do")
