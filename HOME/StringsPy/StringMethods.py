#Converts the first character to upper case 
s = "hello world"
print(s.capitalize()) #"Hello World"

#Returns the number of times a specified value occurs in a string
s = "banana"
print(s.count("a")) #3

#Searches the string for a specified value and returns the position of where it was found
s = "hello"
print(s.find("l")) #2

#Joins the elements of an iterable to the end of the string
lst = ["a", "b", "c"]
print("-".join(lst)) #a-b-c

#Returns True if all characters in the string are in the alphabet
s = "abc"
print(s.isalpha()) #True