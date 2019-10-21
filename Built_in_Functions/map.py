'''
map() is a built-in Python function that takes in two or more arguments: a function and one or more iterables, in the form:
map(function, iterable, ...)
map() returns an iterator - that is, map() returns a special object that yields one result at a time as needed
'''

# List of name [string]
names = ["Joey", "Chandler", "Ross"]
friends = ["Phebes", "Monica", "Rochel"]
relations = map(lambda name, friend: f'{name} is best friend of  {friend}', names, friends)

# Method-1 Printing the relation between them using for loop
for relation_text in relations:
    print(relation_text)

# Method-2 Printing the relation between them using iterator
while True:
    try:
        print(next(relations))
    except StopIteration:
        print('Iteration is over')
        break

