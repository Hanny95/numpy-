import numpy as np

# 연산 시 행, 열 갯수가 맞아야함
# 덧셈 연산
nArr1 = np.array([1,2,3,4,5])
# nArr2 = np.array([3,3,3,3,3])
nArr2 = np.array([3])  # [3,3,3,3,3]
nArr3 = nArr1 + nArr2
print(nArr3)

# 뺄셈 연산
nArr1 = np.array([1,2,3,4,5])
# nArr2 = np.array([3,3,3,3,3])
nArr2 = np.array([3])  # [3,3,3,3,3]
nArr3 = nArr1 - nArr2
print(nArr3)


# 곱셈 연산
nArr1 = np.array([1,2,3,4,5])
# nArr2 = np.array([3,3,3,3,3])
nArr2 = np.array([3])  # [3,3,3,3,3]
nArr3 = nArr1 * nArr2
print(nArr3)


# 나눗셈 연산
nArr1 = np.array([1,2,3,4,5])
# nArr2 = np.array([3,3,3,3,3])
nArr2 = np.array([3])  # [3,3,3,3,3]
nArr3 = np.round(nArr1 / nArr2, 2)  # 소수점 둘째자리에서 반올림 >> np.round함수 이용
print(nArr3)
print(type(nArr3)) # <class 'numpy.ndarray'> : 다차원배열
print(nArr3.dtype)  # float64 (데이터타입 : detype)
# nArr3 = nArr3.astype(int)  # 데이터타입 int로 변경
nArr3 = nArr3.astype('i')  # 데이터타입 int로 변경
print(nArr3)


# 몫 연산
nArr1 = np.array([1,2,3,4,5])
nArr2 = np.array([3])  # [3,3,3,3,3]
nArr3 = nArr1 // nArr2
print(nArr3)


# 나머지 연산
nArr1 = np.array([1,2,3,4,5])
nArr2 = np.array([3])  # [3,3,3,3,3]
nArr3 = nArr1 % nArr2
print(nArr3)

nArr1 = np.array([1,2,3,4,5]).reshape(5, 1)
nArr2 = np.array([3, 3]) # 1행 2열
nArr3 = nArr1 + nArr2
print(nArr3)

# np.dot : 행과 열을 각각 곱해서 더해줌 (정사각형 데이터에서 사용가능)
nArr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
nArr2 = np.dot(nArr1, [[3,3,3],[3,3,3],[3,3,3]])
print(nArr2)

