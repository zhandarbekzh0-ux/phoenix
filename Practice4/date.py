import datetime

now = datetime.datetime.now()
print("Current time:", now)


import datetime

now = datetime.datetime.now()
print("Year:", now.year)
print("Weekday:", now.strftime("%A"))


import datetime

pet_birthday = datetime.datetime(2020, 5, 17)
print("Pet birthday:", pet_birthday)


import datetime

toy_purchase = datetime.datetime(2018, 6, 1)
print("Toy purchased in:", toy_purchase.strftime("%B"))
