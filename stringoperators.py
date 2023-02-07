#String Operators manipulate text and return a string value

# + = Concatenate
# * = Repeat
# [] = Slice
# [:] = Range Slice

name1 = "Marc"
name2 = "Howe"

fullName = name1 + " " + name2
print(fullName)

textValue = "Hello" 

textValue = textValue * 5 # prints out the text 5 times

print(textValue)

textValue = textValue[1] # prints out the character occupying the referenced position, e.g here it's 'e' because 'H' is postion 0

print(textValue)

textValue = textValue[1:5] # Slice a range from 1 (strings start from 0) up until but not including the second position stated

print(textValue)