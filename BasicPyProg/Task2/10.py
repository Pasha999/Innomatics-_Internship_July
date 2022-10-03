# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.

# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.



for i in range(int(input())):
    ele = int(input())
    a = set(map(int, input().split()))

    ele1 = int(input())
    b = set(map(int, input().split()))

    if a.issubset(b):
        print(True)
    else:
        print(False)