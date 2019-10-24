"""
 Guess a number between 100 until finishes

 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/24/2019
 Time: 10:12 PM
 """

from random import randint

answer = randint(1, 100)
counter = 0
while True:
    counter += 1
    guess = int(input("Guess a number (1-100) : "))
    if guess > answer:
        print("its little number try again.")
    elif guess < answer:
        print("its big number try again.")
    else:
        print("Boooooooom! You did it")
        break
if counter > 10:
    print("Sorry to say.! Your IQ is very low.")
