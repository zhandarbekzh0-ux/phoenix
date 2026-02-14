def show_number():
    number = 300
    print(number)

show_number()


def outer_box():
    item_count = 300
    def inner_box():
        print(item_count)
    inner_box()

outer_box()


total_items = 300

def print_total():
    print(total_items)

print_total()
print(total_items)


def change_word():
    word = "Apple"
    def modify():
        nonlocal word
        word = "Banana"
    modify()
    return word

print(change_word())


place = "outside"

def room():
    place = "inside"
    def drawer():
        place = "small box"
        print("Drawer:", place)
    drawer()
    print("Room:", place)

room()
print("Global:", place)
