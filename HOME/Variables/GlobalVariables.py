name = "Zhandarbek"
def nfunc():
    print("My name is " + name)

nfunc()  #This variable is global because it is declares outside of any function

car = "Lada Kalina"
def cartuning():
    global car
    car = "Lada Priora"

cartuning() #We can modify global value inside of function

num = 5
def numbb():
    print(num)

print(num) #We can read a global variable inside a function without any extra keywords

j = 67
def sixseven():
    global j
    j+=2
sixseven() #We can modify values of variables

