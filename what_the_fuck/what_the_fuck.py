"""
Don't let return and finally meet!
Really terrible!
"""
def return_and_finally():
    try:
        return 'from_try'
    finally:
        return 'from_finally'
        
print(return_and_finally())
"""
You will surprising find from_finally on the screen!
How can that happen!
Actually,when break, continue or return in try sentence, and exactly there is a finally sentence...
It will run finally first!
"""



"""
l thought l would see two True on the screen...
"""
print('what' * 5 is "whatwhatwhatwhatwhat")
print('what' * 6 is "whatwhatwhatwhatwhatwhat")
"""
But actually...
One True and One False
How can that happan!
eee...Because of the existance of constant folding...
a powerful technology...
constant folding in python will convert a string with less than twenty characters.
But if the string has more than two characters, python will not convert it.
Think about pyc's feeling!
"""



"""
If the first two is correct...
It seems like all the sentences below can run correctly...
"""
print('right?''')
print("right?""")
#print('''right?')
#print("""right?")
"""
But actually not!It will cause a Syntax Error.
You can use three double quotes or three single quotes to end a string.
But if the scanner first get three double quotes or single,it will try to find another.
If there is not another,it will raise a Syntax Error.Surprising?Yes?
"""



"""
Let me see...
one int, two bool...
"""
various_list = [1.5, 3, "string", True, False]
integers = 0
booleans = 0
for item in various_list:
    if isinstance(item, int):
        integers += 1
    elif isinstance(item, bool):
        booleans += 1
print(integers, booleans)
"""
what!three and zero!
How to explain this!
eee...Oh, it's because True == 1 and False == 0!
That is really confusing but reasonable...
"""



"""
You are changing the tuple all the time.How can you do this!
"""
another_tuple = ([1, 2], [3, 4], [5, 6])
another_tuple[2].append(1000)
print(another_tuple)
try:
	another_tuple[2] += [99, 999]
except Exception as e:
	print(e)
print(another_tuple)
a = [10,20]
tuple_first = (50, 60, a)
print(tuple_first)
a += [30,40]
print(tuple_first)
"""
Yeah, l am wrong...
only one error...
It seems like if there is a changeable thing like list in a tuple,you can change the list with append or extend.
But += is the combination of extend and =,so...
Oh, l understand!Extend has no error, so the tuple has been changed, and then = has an error.
That's amazing!l can change the tuple, l can not wait to show this skill to my friends!
"""
