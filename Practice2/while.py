stick = 1
while stick < 6:
    print(stick)
    stick += 1

stone = 1
while stone < 6:
    print(stone)
    if stone == 3:
        break
    stone += 1

apple = 0
while apple < 6:
    apple += 1
    if apple == 3:
        continue
    print(apple)

step = 1
while step < 6:
    print(step)
    step += 1
else:
    print("Steps finished")
