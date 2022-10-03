# You have a non-empty set s, and you have to execute N commands given in N lines.

# The commands will be pop, remove and discard.






n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    s1 = input().split()
    if s1[0] == 'pop':
        s.pop()
    elif s1[0] == 'remove':
        s.remove(int(s1[1]))
    elif s1[0] == 'discard':
        s.discard(int(s1[1]))
        
print(sum(s))