import sys
sys.stdin = open("p1948. 날짜 계산기.txt", "r")

"""
[방법1]
"""
# T = int(input())
# date_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# for t in range(1, T + 1):
#     start_month, start_date, end_month, end_date = map(int, input().split())

#     date = 0
#     for month in range(start_month, end_month):
#         date += date_list[month]
    
#     result = date + (end_date - start_date + 1)
#     print(f'#{t} {result}')

"""
[방법2] 누적 date list

cf) date_list에 0을 하나 더 추가해준 이유는 1/1 2/28 생각해보면 됨.
"""
T = int(input())
date_list = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

for t in range(1, T + 1):
    start_month, start_date, end_month, end_date = map(int, input().split())
    result = (date_list[end_month] - date_list[start_month]) + (end_date - start_date + 1)
    print(f'#{t} {result}')