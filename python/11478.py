import sys

s = sys.stdin.readline().strip()
result = set()
for i in range(1,len(s)+1):
    for j in range(len(s)+1-i):
        result.add(s[j:j+i])

print(len(result))