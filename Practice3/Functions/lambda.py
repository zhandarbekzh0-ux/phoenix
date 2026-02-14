add_apples = lambda apples: apples + 5
print(add_apples(3))


def make_multiplier(factor):
    return lambda price: price * factor

double_price = make_multiplier(2)

print(double_price(11))


pencils = [1, 2, 3, 4, 5]
more_pencils = list(map(lambda p: p * 2, pencils))
print(more_pencils)


chairs = [1, 2, 3, 4, 5, 6, 7, 8]
even_chairs = list(filter(lambda c: c % 2 == 0, chairs))
print(even_chairs)


workers = [("Ali", 25), ("Sara", 22), ("Omar", 28)]
sorted_workers = sorted(workers, key=lambda person: person[1])
print(sorted_workers)
