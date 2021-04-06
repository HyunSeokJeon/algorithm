
cnt = 1
det = 1
N = input()
N = int(N)
while True:
    if N <= det:
        break
    else:
        det += 6 * cnt
        cnt += 1

print(cnt)