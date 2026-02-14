def print_color(color):
    print(color + " color")

print_color("Red")
print_color("Blue")
print_color("Green")


def greet(person): 
    print("Hi", person)

greet("Ali")  


def combine_words(word1, word2):
    print(word1 + " " + word2)

combine_words("Big", "House")


def choose_drink(drink="Water"):
    print("You chose", drink)

choose_drink("Juice")
choose_drink("Milk")
choose_drink()
choose_drink("Tea")


def show_items(items):
    for item in items:
        print(item)

things = ["pen", "book", "cup"]
show_items(things)
