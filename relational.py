x = 10
y = 15
z = 10.0

print(x > y) # False

print(x < y) # True

print(x == y) # False

print(x !=y) # True

print(x == 10) # True

if(x > y):
    print("X is bigger than Y!")
else:
    print("Y is bigger than (or equal to) X!")

#
# AND - both sides need to be true to equal True, if one side or both are False, then False will be the answer, e.g.

print( x == 10 and y == z ) # The first statement is True, but the second is False. As both sides are not True, the output is False

# OR - Opposite of above. Only one side needs to be True for the output to be True. Only if both sides are False, the output is False. 

print( x == 10 or y == z ) # As above, the first statement is True but the second statement is false; as at least one side is True, the output is True

