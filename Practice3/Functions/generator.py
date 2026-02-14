def number_box():
    yield 10
    yield 20
    yield 30

for item in number_box():
    print(item)


def give_tickets(limit):
    ticket = 1
    while ticket <= limit:
        yield ticket
        ticket += 1

for t in give_tickets(5):
    print(t)


cup_list = [c * 2 for c in range(5)]
print(cup_list)

cup_gen = (c * 2 for c in range(5))
print(cup_gen)
print(list(cup_gen))


def growing_numbers():
    x, y = 1, 1
    while True:
        yield x
        x, y = y, x + y

gen = growing_numbers()
for _ in range(10):   
    print(next(gen))


def repeat_machine():
    while True:
        word = yield
        print("You said:", word)

machine = repeat_machine()
next(machine) 
machine.send("Hi")
machine.send("Bye")
