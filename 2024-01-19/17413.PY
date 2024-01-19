import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline

S = input() + " "
stack = deque()
ans = ""
flag = 0
for x in S:
    if x == "<":
        flag = 1
        while stack:
            ans += stack.pop()
    stack += x
    if x == ">":
        flag = 0
        while stack:
            ans += stack.popleft()
    if (x == " " and flag == 0):
        stack.pop()
        while stack:
            ans += stack.pop()
        ans += " "
print(ans.rstrip())
