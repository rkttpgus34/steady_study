import sys

sys.stdin = open("input.txt")

H, M = map(int, input().split())

if M < 45:
    M = M + 60 - 45
    if H == 0:
        H = H + 24 - 1
    else:
        H = H - 1
else:
    M -= 45

print(H, M)