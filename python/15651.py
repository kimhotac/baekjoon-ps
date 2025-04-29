import sys

n, m = map(int,sys.stdin.readline().split())

def backtrack(path):
    if len(path) == m:
        print(' '.join(map(str,path)))
        return
    for i in range(1,n+1):
        backtrack(path+[i])
backtrack([])