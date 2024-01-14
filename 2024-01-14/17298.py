import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input()))

stack = []

for i in arr:
    

