"""
[방법1]
"""
# N = int(input())
# number_str = input()

# sumNum = 0
# for idx in range(len(number_str)):
#     sumNum += ord(number_str[idx]) - ord('0')
# print(sumNum)

"""
[방법2]
"""
# N = int(input())
# number_str = input()

# sumNum = 0
# for idx in range(len(number_str)):
#     sumNum += int(number_str[idx])
# print(sumNum)


"""
[방법3]
"""
N = int(input())
sumNum = sum(map(int, input()))
print(sumNum)