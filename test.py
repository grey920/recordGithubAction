import requests 
from bs4 import BeautifulSoup

# 리디북스의 IT 베스트셀러 목록 조회
url = 'https://ridibooks.com/category/bestsellers/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

# 책 제목의 태그 class명이 title_text이다.
bookservices = soup.select('.title_text')
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip()) #text.strip(): 앞뒤공백 제거
