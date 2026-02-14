def remove_blocks(n):
    if n <= 0:
        print("No blocks left!")
    else:
        print("Removing block", n)
        remove_blocks(n - 1)

remove_blocks(5)


def stack_chairs(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * stack_chairs(n - 1)

print(stack_chairs(5))


def biggest_stone(stones):
    if len(stones) == 1:
        return stones[0]
    else:
        biggest_rest = biggest_stone(stones[1:])
        return stones[0] if stones[0] > biggest_rest else biggest_rest

stone_list = [3, 7, 2, 9, 1]
print(biggest_stone(stone_list))


def count_coins(coins):
    if len(coins) == 0:
        return 0
    else:
        return coins[0] + count_coins(coins[1:])

coin_list = [1, 2, 3, 4, 5]
print(count_coins(coin_list))

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
