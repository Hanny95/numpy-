import numpy as np

# 7행 8열 배열 생성
nArr = np.arange(56).reshape(7, 8)
print(nArr)

print(nArr[1, 3]) # 2행 4열
print(nArr[0, 4]) # 1행 5열
print(nArr[-1, 2]) # 마지막행 3열
print(nArr[2, 1:5]) # 3행 2~5열
print(nArr[5, (0,2,3)]) # 6행 1,3,4열
print(nArr[4, 0]) # 5행 1열
print(nArr[1, -1]) # 2행 마지막열
print(nArr[1,:]) # 2행의 모든데이터
print(nArr[:,4]) # 5열의 모든데이터
print(nArr[:,3]) # 4열 미만의 모든데이터
print(nArr[:,2:4]) # 2열 초과 5열 미만의 모든데이터
print(nArr[::2,:]) # 홀수행의 모든데이터
print(nArr[1::2,:]) # 짝수행의 모든데이터
print(nArr[:,::2]) # 홀수열의 모든데이터
print(nArr[:,1::2]) # 짝수열의 모든데이터
print(nArr[5, 2:6]) # 6행 3~6열
print(nArr[5, 2:]) # 6행 3~마지막열까지
print(nArr[2, ::2]) # 3행 처음부터마지막열까지 2단계
print(nArr[1, :-1:2]) # 2행 처음부터마지막에서 두번째까지 2단계 출력
print(nArr[::3, :-1:2]) # 첫행~마지막행 3단계 , 처음~마지막두번째 열 2단계 출력