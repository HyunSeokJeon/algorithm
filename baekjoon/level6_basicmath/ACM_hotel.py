n = int(input())
cases = []
for _ in range(n):
    put = input()
    case = put.split()
    cases.append(case)

for case in cases:
    h = int(case[0])
    w = int(case[1])
    n = int(case[2])
    roomNum = n // h + 1
    floorNum = n % h
    if floorNum == 0:
        floorNum = h
        roomNum -= 1
    answer = floorNum * 100 + roomNum

    print(answer)
