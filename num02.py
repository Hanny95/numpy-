import numpy as np

nArr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# 다차원배열의 모든 아이템 요소의 합 구하기(sum)
sha = nArr.shape

sum = 0

for i in range(sha[0]):
    for j in range(sha[1]):

        sum = sum + nArr[i][j]

print(sum)

# 재귀함수(함수내에서 나를 다시 호출,,)를 이용해서 다차원 배열의 합 구하기

# def sum():
#
#     sum = 0
#
#     for i in range(sha[0]):
#         for j in range(sha[1]):
#             sum = sum + nArr[i][j]
#
#     return sum

