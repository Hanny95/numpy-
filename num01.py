import numpy as np
import random

# numpy 버전 확인
print({np.__version__})

# 배열
# 2차원 배열
# listVars = [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
# ]
# print(listVars[0]) # [1, 2, 3]
# print(listVars[0][0])  # 1
# print(listVars[0][1])  # 2
# print(listVars[0][2])  # 3

# 배열
# nums1 = [1,2,3]
# nArr = np.array(nums1)
# print(f'nArr : {nArr}') #[1 2 3] > numpy 배열은 쉼표가 없다
# print(f'nArr type : {type(nArr)}')
# print(f'nArr type : {len(nArr)}')
#
# print(f'shape : {np.shape(nArr)}') # shape : (3,) > 데이터 3개인 튜플
# print(f'shape idx[0] : {np.shape(nArr[0])}')

# 2차원 배열 [[, , ,], [, , ,], [, ,]]
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# nArr = np.array([nums1, nums2])
# print(f'nArr : {nArr}')
# print(f'shape : {nArr.shape}')
#
# # 3행 3열
# nArr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(f'nArr2 : {nArr2}')
# print(f'shape : {nArr2.shape}')

# 5행 2열 배열을 만들고, 모양을 출력해보자
# 2행 5열 배열을 만들고 모양 출력
#
# data1 = [1,2,3,4,5]
# data2 = [6,7,8,9,10]
# dataArr = np.array([data1, data2])
# print(f'dataArr : {dataArr}')
# print(f'shape : {dataArr.shape}')  # shape : (2, 5)
#
# charDatas = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
# print(f'charDatas : {charDatas}')
# print(f'shape : {charDatas.shape}')   # shape : (5, 2)


# for문을 이용해서 2행 3열 다차원배열을 만들고 모양(shape)출력

# cnt = 0
# nsOutter = []
# for i in range(2):
#     ns1 = []
#     for j in range(3):
#        cnt += 1
#        ns1.append(cnt)
#
#     nsOutter.append(ns1)
#
# nums = np.array(nsOutter)
# print(f' nums : {nums}')
#
# name = ['이름', '박찬호', '박세리', '이승엽', '박지성', '김연경']
# age = ['나이', 46, 20, 19, 40, 20]
# sport = ['종목', '야구', '골프', '야구', '축구', '배구']
# country = ['국적', '한국', '한국', '한국', '한국', '한국']
# sex = ['성별', 'M', 'W', 'M', 'M', 'W']
#
# # datas = np.array([[name], [age], [sport], [country], [sex]])
# datas = np.array([name, age, sport, country, sex])
# print(f'{datas}')
# print(f'shape : {datas.shape}')

# size, ndim(몇차원인지), shape(데이터모양)
# nArr = np.array([[1,2,3], [4,5,6]])
# print(f' nArr : {nArr}')
# print(f' nArr : {type(nArr)}')  #  nArr : <class 'numpy.ndarray'>
# print(f'size : {nArr.size}')  # size : 6
# print(f'ndim : {nArr.ndim}') # ndim : 2  >> 2차원 배열
# print(f'shape : {nArr.shape}')  # shape : (2, 3)

# 3차원 배열만들기
# nArr = np.array([[[1, 2], [3, 4], [5, 6]]])
# print(f'nArr : {nArr}')
# print(f'nArr size: {nArr.size}')  # nArr size: 6
# print(f'nArr ndim: {nArr.ndim}')  # nArr ndim: 3
# print(f'nArr shape: {nArr.shape}')  # nArr shape: (1, 3, 2)

# 다차원배열 - reshape
# nArr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(f'nArr : {nArr}')
# print(f'nArr shape: {nArr.shape}')

# 5행 2열로 바꾸기 (reshape)이용
# r_nArr = nArr.reshape(5, 2)
# print(f'r_nArr : {r_nArr}')
# print(f'r_nArr : {np.shape(r_nArr)}')

# zeros
# nArr = np.zeros((2,5))  # 튜플형식으로 데이터 주기 () 필수!
# print(f'nArr : {nArr}')  # 데이터 타입 : float
# print(f'nArr : {nArr.shape}')
# print(type(nArr[0][0]))


# ones
# nArr = np.ones((5,2))
# print(f'nArr : {nArr}')  # 데이터 타입 : float
# print(f'nArr : {nArr.shape}')


# data search
nArr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(f'nArr[0][0] : {nArr[0][0]}')
print(f'nArr[0][1] : {nArr[0][1]}')
print(f'nArr[0][2] : {nArr[0][2]}')
print(f'nArr[0][3] : {nArr[0][3]}')
print(f'nArr[0][4] : {nArr[0][4]}')

print(f'nArr[1][0] : {nArr[1][0]}')
print(f'nArr[1][1] : {nArr[1][1]}')
print(f'nArr[1][2] : {nArr[1][2]}')
print(f'nArr[1][3] : {nArr[1][3]}')
print(f'nArr[1][4] : {nArr[1][4]}')

# cnt = 0
# nsOutter = []
# for i in range(2):
#     ns1 = []
#     for j in range(3):
#        cnt += 1
#        ns1.append(cnt)
#
#     nsOutter.append(ns1)
#
# nums = np.array(nsOutter)

# 반복문을 이용해서 다차원배열의 모든 데이터 조회하기

shape = nArr.shape
ndim = nArr.ndim
size = nArr.size
print(shape[1])
print(size)


for i in range(shape[0]):
    for j in range(shape[1]):
       print(nArr[i][j])

# shape 가 (2, 3, 4)인 다차원 배열 만들기
# random 모듈 이용

sha = 2, 3, 4
nArr = np.zeros(sha)

for r1 in range(sha[0]):
    for r2 in range(sha[1]):
        for r3 in range(sha[2]):
            nArr[r1][r2][r3] = random.randint(0, 10)

print(f'nArr : {nArr}')

