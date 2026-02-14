def make_loud(func):
    def wrapper():
        return func().upper()
    return wrapper

@make_loud
def say_word():
    return "good morning"

print(say_word())


def make_loud(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

@make_loud
def greet_person(person):
    return "hi " + person

print(greet_person("Ali"))


def simple_message():
    return "Drink water"

print(simple_message.__name__)


def make_loud(func):
    def wrapper():
        return func().upper()
    return wrapper

@make_loud
def advice():
    return "wash your hands"

print(advice.__name__)  


import functools

def make_loud(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@make_loud
def reminder():
    return "close the door"

print(reminder.__name__) 
