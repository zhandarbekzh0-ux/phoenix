x = y = z = "Multiple value" #All variables contains a same value

lang = ["C++", "Python", "Java"]
x = y = z = lang
print(z)  #We can unpack tuples and lists, etc.

x, y, z = 5, 7, 9 #We can assign values to many variables in one line

x, y = 5, 4
x, y = y, x
print(x, y) #We can swap values

r = (1, 3, 90)
print(r[1]) # WE can store multiple values