"""
 verify user

 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/23/2019
 Time: 8:40 PM
 """
from getpass import *

user = input("user : ")
password = getpass("password : ")

if user == "admin" and password == "123456":
    print("successfully logged in")
else:
    print("invalid user or password")
