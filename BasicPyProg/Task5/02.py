# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
match = re.search(r"([a-zA-Z1-9])\1",input())
print(match.group(1) if match else -1)