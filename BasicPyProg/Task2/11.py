# Objective
# Today, we're learning about a new data type: sets.

# Concept

# If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list. The delimiter is space (ascii 32) by default. To specify that comma is the delimiter, use string.split(','). For this challenge, and in general on HackerRank, space will be the delimiter.



M = int(input())
a = set(input().split())
N = int(input())
b = set(input().split())

list1 = list(map(int,a.difference(b)))
list2 = list(map(int,b.difference(a)))

new = list1 + list2

sorted_list = sorted(new)

for i in sorted_list:
    print(i)