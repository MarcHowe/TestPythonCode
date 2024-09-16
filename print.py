print() # Prints a new line character (\n) 
print("Hello") # The thing(s) we want to print out must live in the first positional parameter, other paramaters can follow in any order

myName = "Marc"
print(myName)

print("Hello",myName,"How","are","you?") # Prints out the string and variable value, but notice the output places a space between the objects

# When objects are passed to print as a standalone variable (using commas to separate, no concatenation) print will attempt to cast non-string values into a string:
age = 39
print("Hello", "Marc", "You are:", age, "years old.") 

# Used in the following way generates an error; because concatenate doesn't know if this is an addition or concatenation: 
age = 39
#print("Hello", "Marc", "You are:" + age + "years old.") 


# Print parameters Sep, End and File

# Sep = How to seperate in the instance of multiple objects
# End = What to print at the end
# File = Redirect output to a file on the file system

fileObject = open("output.txt", mode="w") # Handle/File object opens with write permissions - this overwrites the contents each time
print("Hello Marc!", file=fileObject)

print("Hello", "Marc", "Howe", sep = ":") # Output is Hello:Marc:Howe

print("hello", end="")
print("Goodbye") # output is helloGoodbye