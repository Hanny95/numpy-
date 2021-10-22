import numpy as np
import copy

# View 개념 : 메모리를 효율적으로 사용하기 위해 도입 (but 원본데이터 훼손됌)
nArr = np.arange(25).reshape(5, 5)
print(nArr)

print(nArr[2][:])

# 3행
# row3 = nArr[2][:]
# print(row3) # [10 11 12 13 14] 리스트로 출력
# # 인덱스로 데이터 수정
# row3[2] = 99
# print(row3)
#
# print(nArr)  #>> 원본데이터도 같이 변경 (numpy의 view 개념)
#
# row3[2:] = [102, 103, 104]
# print(row3)
# print(nArr)   #>> 원본데이터도 같이 변경 (numpy의 view 개념)

# ! copy.copy를 이용해 원본데이터 유지 !
row3 = copy.copy(nArr[2, :])
print(row3)

row3[2] = 99
print(row3)
print(nArr) # >> 원본데이터 훼손 안됌!!