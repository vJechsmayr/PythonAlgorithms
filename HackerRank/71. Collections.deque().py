# Author Aman Shekhar

from collections import deque
d = deque()
for i in range(int(input())):
    q = list(map(str,input().split()))
    if q[0] == "append":
        d.append(int(q[1]))
    elif q[0] == "pop":
        d.pop()
    elif q[0] == "popleft":
        d.popleft()
    elif q[0] == "appendleft":
        d.appendleft(int(q[1]))
print(*d)