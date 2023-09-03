import sys

sys.stdin = open("input.txt")

n = int(input())

print(n*(n+1)//2)