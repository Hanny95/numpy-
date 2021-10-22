import numpy as np
from urllib import request as rq
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import saveToExcel as s2e

# 배열 arange
nArr1 = np.arange(0, 12, 1) # 0, 1, 2.....11
print(nArr1)

# reshape > 3행 4열
r_nArr1 = nArr1.reshape(3, 4)
print(r_nArr1)

r_nArr1 = r_nArr1.reshape(1, 12)
print(r_nArr1)

# nArr1 에서 reshape 할 수 있는 모든 경우를 출력해보기
# for i in range(1, num1 + 1):
#   if (num1 % i == 0) & (num2 % i == 0):
#     gcd = i

# 주식정보를 가져와서 다차원 배열로 저장하기

url = 'https://finance.naver.com/sise/lastsearch2.naver'
browser = webdriver.Chrome()
browser.get(url)

ranking = browser.find_elements(By.CLASS_NAME, 'no')
companyName = browser.find_elements(By.CLASS_NAME, 'tltle')
searchRatioCss = '#contentarea > div.box_type_l > table > tbody > tr > td:nth-child(3)'
priceCss = '#contentarea > div.box_type_l > table > tbody > tr > td:nth-child(4)'
gapCss = '#contentarea > div.box_type_l > table > tbody > tr > td:nth-child(5)'
fluctuationRateCss ='#contentarea > div.box_type_l > table > tbody > tr > td:nth-child(6)'


searchRatio = browser.find_elements(By.CSS_SELECTOR, searchRatioCss)
price = browser.find_elements(By.CSS_SELECTOR, priceCss)
gap = browser.find_elements(By.CSS_SELECTOR, gapCss)
fluctuationRate = browser.find_elements(By.CSS_SELECTOR, fluctuationRateCss)

# rank = np.array(ranking)
# r_rank = rank.reshape(1, 30)
# # print(r_rank)
for idx, n in enumerate(price):
    print(idx+1, n.text)

cnt = 0
ns2 = []

try:
    for i in range(ranking):
        ns = []
        for j in range(companyName):
            cnt += 1
            ns.append(cnt)

        ns2.append(ns)

    result = np.array(ns2)

except Exception as e:
    print(e)

else:
    print('success')