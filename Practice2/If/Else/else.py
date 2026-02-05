kid1_height = 200  
kid2_height = 33   

if kid2_height > kid1_height:
    print("Kid 2 is taller than Kid 1")
elif kid1_height == kid2_height:
    print("Both kids are the same height")
else:
    print("Kid 1 is taller than Kid 2")

bag1_weight = 200  
bag2_weight = 33    

if bag2_weight > bag1_weight:
    print("Bag 2 is heavier than Bag 1")
else:
    print("Bag 2 is not heavier than Bag 1")

apples = 7

if apples % 2 == 0:
    print("Even number of apples")
else:
    print("Odd number of apples")

current_temp = 22 

if current_temp > 30:
    print("It's hot outside!")
elif current_temp > 20:
    print("It's warm outside")
elif current_temp > 10:
    print("It's cool outside")
else:
    print("It's cold outside!")

fruits_in_basket = "apples"

if len(fruits_in_basket) > 0:
    print(f"You have {fruits_in_basket} in the basket!")
else:
    print("The basket is empty!")
