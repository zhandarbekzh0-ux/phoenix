person_age = 25
has_watering_can = True

if person_age >= 18:
    if has_watering_can:
        print("You can water the garden")
    else:
        print("You need a watering can")
else:
    print("You are too young to water the garden")

homework_score = 85
class_attendance = 90
homework_submitted = True

if homework_score >= 60:
    if class_attendance >= 80:
        if homework_submitted:
            print("Homework completed successfully")
        else:
            print("Homework missing a submission")
    else:
        print("Homework ok but low attendance")
else:
    print("Homework failed")

current_temp = 25
is_clear_sky = True

if current_temp > 20:
    if is_clear_sky:
        print("Perfect weather for a picnic!")

garden_temp = 25
sunny_day = True

if garden_temp > 20:
    if sunny_day:
        print("Ideal conditions to water the flowers!")

card_name = "LibraryCard123"
card_valid = True
card_active = True

if card_name:
    if card_valid:
        if card_active:
            print("You can borrow books")
        else:
            print("Card is inactive")
    else:
        print("Card is invalid")
else:
    print("No card provided")
