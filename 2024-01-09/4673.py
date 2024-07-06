import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

a = [0 for _ in range(10001)]

for i in range(1,10000):
    sum = i
    while i:    
        sum += i % 10
        i = i // 10
    if sum <= 10000:
        a[sum] = 1

for i in range(1,10000):
    if a[i] == 0:
        print(i)