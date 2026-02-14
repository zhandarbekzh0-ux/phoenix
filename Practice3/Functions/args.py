def show_box(*items):
    print("Type:", type(items))
    print("First item:", items[0])
    print("Second item:", items[1])
    print("All items:", items)

show_box("pen", "pencil", "eraser")


def add_prices(*prices):
    total = 0
    for price in prices:
        total += price
    return total

print(add_prices(1, 2, 3))
print(add_prices(10, 20, 30, 40))
print(add_prices(5))


def show_student(**student):
    print("Last name is " + student["last"])

show_student(first="Ali", last="Smith")


def print_person(**info):
    print("Type:", type(info))
    print("Name:", info["name"])
    print("Age:", info["age"])
    print("All info:", info)

print_person(name="Sara", age=25, city="Astana")


def add_three(x, y, z):
    return x + y + z

values = [4, 5, 6]
result = add_three(*values)  
print(result)
