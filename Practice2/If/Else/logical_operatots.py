basket_apples = 200
basket_oranges = 33
basket_pears = 500

if basket_apples > basket_oranges and basket_pears > basket_apples:
    print("Both conditions are met: Apples > Oranges AND Pears > Apples")

smallbottle = 200
mediumbottle = 33
largebottle = 500

if smallbottle > mediumbottle or smallbottle > largebottle:
    print("At least one condition is True: Small bottle > Medium OR Small bottle > Large")

chairs1 = 33
chairs2 = 200

if not chairs1 > chairs2:
    print("Room 1 does NOT have more chairs than Room 2")

buyer_age = 25
is_member = False
has_coupon = True

if (buyer_age < 18 or buyer_age > 65) and not is_member or has_coupon:
    print("Discount applies for this buyer!")
