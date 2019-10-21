"""
 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/20/2019
 Time: 8:48 PM
 
 """

str1 = 'hello, world!'
print('str1 length:', len(str1))
print('str1 title: ', str1.title())
print('str1 uppercase: ', str1.upper())
str1 = str1.upper()
print('str1 is uppercase?: ', str1.isupper())
print('str1 startswith hello?: ', str1.startswith('hello'))
print('str1 endswith hello?: ', str1.endswith('hello'))
print('str1 startswith !?: ', str1.startswith('!'))
print('str1 endswith !?: ', str1.endswith('!'))
str2 = '- ওহে বিশ্ব!'
str3 = str1.title() + ' ' + str2.lower()
print(str3)
