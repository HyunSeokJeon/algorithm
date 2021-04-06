a = int(input())
cnt = 1
stand = 0
while True:
    stand = (1 + cnt) * cnt / 2
    if a <= stand:
        break
    cnt += 1
front = 0
back = 0
if cnt % 2 != 0:
    oddCase = stand - a
    front = 1 + oddCase
    back = cnt - oddCase
else:
    evenCase = stand - a
    front = cnt - evenCase
    back = 1 + evenCase

print(int(front), '/', int(back), sep='')