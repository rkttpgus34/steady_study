import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

print(2**(int(input())))