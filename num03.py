import numpy as np

# 단위행렬

nArr = np.eye(1)
print(f'nArr : {nArr}')

nArr = np.eye(2)
print(f'{nArr}')

nArr = np.eye(3)
print(f'{nArr}')


# 행렬 곱셈 > 행과 열이 같아야함
nArr1 = np.eye(2)
nArr2 = np.array([[10,20], [30, 40]])

nArr3 = nArr1 * nArr2
print(f'{nArr3}')

# dot
nArr3 = np.dot(nArr1, nArr2)
print(f'{nArr3}')

# 곱셈 & 행렬 곱셈
# [[2, 4, 6], [7, 3, 11]]
# [[7, 2, 3], [8, 2, 2]]

arr1 = np.array([[2, 4, 6], [7, 3, 11],[2, 5, 4]])
arr2 = np.array([[7, 2, 3], [8, 2, 2], [2, 5, 4]])


arr3 = arr1 * arr2
print(arr3) # [[14  8 18]
            # [56  6 22]]

arr3 = np.dot(arr1, arr2)
print(arr3)
# 스스로하기..
# 다차원 배열에서 처음과 마지막요소를 찾고 합 구하기
# 0을 포함한 짝수행, 0을 포함한 짝수열 의 합 구하기
shpae = arr3.shape
print(shpae)

for i in range(shpae[0]):
    n1 = arr3[0][0]
    for j in range(shpae[1]):
        n2 = arr3[2][2]
        print(n1 + n2)


