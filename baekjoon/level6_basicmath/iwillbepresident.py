# t = int(input())
# test_cases = []
# for _ in range(t):
#     k = int(input()) # 층
#     n = int(input()) # 호수
#     test_cases.append([k, n])
# sum = 0
# kCheck = True
# if k == 0:
#     kCheck = False
# while kCheck:
#     for n in range(1, n+1):
#         sum += n
import time

t = int(input())
test_cases = []
for _ in range(t):
    k = int(input()) # 층
    n = int(input()) # 호수
    test_cases.append([k, n])
# starttime = time.time()

# def underfloor(k, n):
#     if k == 0:
#         return n
#     else:
#         sum = 0
#         for i in range(n+1):
#             sum += underfloor(k-1, i)
#         return sum
# for case in test_cases:
#     k = case[0]
#     n = case[1]
    
#     print(underfloor(k, n))

# print(time.time() - starttime)




