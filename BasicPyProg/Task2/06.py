# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.

# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.






A = set(input().split())
COUNT = 0
VALUE = 0
for i in range(int(input())):
    n = set(input().split())
    if A == n:
        VALUE += 1
    elif A.issuperset(n):
            COUNT += 1
    else:
        VALUE += 1
if VALUE != 0:
    print('False')
else:
    print('True')