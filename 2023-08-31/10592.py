import sys

sys.stdin = open("input.txt")

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print(a + b)