import sys

sys.stdin = open("input.txt")

MAX = 1
MIN = 1000000

N = int(input())
arr = list(map(int, input().split()))

for i in arr:
    if MAX < i:
        MAX = i
    if MIN > i:
        MIN = i

print(MIN, MAX)