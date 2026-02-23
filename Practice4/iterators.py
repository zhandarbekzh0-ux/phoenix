toys = ("car", "ball", "doll")
toy_iter = iter(toys)

print(next(toy_iter))
print(next(toy_iter))
print(next(toy_iter))


toys = ("car", "ball", "doll")

for t in toys:
    print(t)


class StickCounter:
    def __iter__(self):
        self.stick = 1
        return self

    def __next__(self):
        s = self.stick
        self.stick += 1
        return s

sticks = StickCounter()
stick_iter = iter(sticks)

print(next(stick_iter))
print(next(stick_iter))
print(next(stick_iter))
print(next(stick_iter))
print(next(stick_iter))

class StickCounter:
    def __iter__(self):
        self.stick = 1
        return self

    def __next__(self):
        if self.stick <= 10:
            s = self.stick
            self.stick += 1
            return s
        else:
            raise StopIteration

sticks = StickCounter()
stick_iter = iter(sticks)

for s in stick_iter:
    print(s)
