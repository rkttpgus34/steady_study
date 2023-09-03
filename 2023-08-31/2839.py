import sys

sys.stdin = open("input.txt")

N = int(input())

Five = N // 5
rep = Five

for i in range(rep + 1):
    rem = N - 5 * Five
    if rem % 3 == 0:
        print(Five + rem // 3)
        break
    else:
        Five -= 1

else:
    print(-1)
