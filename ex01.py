import numpy as np
# 6 X 6 행렬
nArr = np.arange(36).reshape(6, 6)
print(nArr)

# 데이터 찾기 > 인덱스 이용
print(nArr[1][2])
print(nArr[4][1])

# 3차원
# print(nArr[1][2][2])

# 데이터 찾기 > numpy
print(nArr[1, 2])
print(nArr[4, 1])

# 3행의 1,3,5열
print(nArr[3, [1,3,5]])

# 파이썬 슬라이싱
numbers = [2, 50, 0.12, 1, 9, 7, 17, 35, 100, 3.14]
print(numbers[1:6])
print(numbers[1:])
print(numbers[:6])
print(numbers[1::2])
print(numbers[::2])
print(numbers[1:-1])
print(numbers[-5:-2])


# numpy 슬라이싱
nArr = np.arange(36).reshape(6, 6)

# row 조회
print(nArr[1,])
print(nArr[1,:])  # numpy 에서 :(콜론)은 전체선택
print(nArr[(1, 4),])
print(nArr[:,:]) # 모든행, 모든열
print(nArr[(1,2,3),])
print(nArr[1:4,])
print(nArr[1:4:2,])

# column 조회 (비워둘수없음 , 전체선택시 :(콜론)이용)
print(nArr[:,1])  # 모든 1열 (일차원배열)
print(nArr[:,1:4]) # 모든 1~3열  (이차원배열)
print(nArr[:,:2])


# row & column 조회
print(nArr[2:5,1:4])
print(nArr[2:5, ::2])
print(nArr[::2, ::3])
print(nArr[0, :-2])
print(nArr[-1, -1])

