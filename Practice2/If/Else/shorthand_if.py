basket1_apples = 5
basket2_apples = 2
if basket1_apples > basket2_apples:
    print("Basket 1 has more apples than Basket 2")

pencils_alice = 2
pencils_bob = 330
print("Alice") if pencils_alice > pencils_bob else print("Bob")

apple_weight = 10
orange_weight = 20
heavier_fruit = apple_weight if apple_weight > orange_weight else orange_weight
print("Heavier fruit weighs", heavier_fruit, "grams")

chosen_snack = ""
snacktoeat = chosen_snack if chosen_snack else "Cookie"
print("Snack for today:", snacktoeat)

bottle1 = 15
bottle2 = 20
larger_bottle = bottle1 if bottle1 > bottle2 else bottle2
print("Larger bottle contains:", larger_bottle, "liters")
