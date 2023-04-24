import streamlit as st
import pandas as pd

# 데이터 프레임 생성
data = pd.DataFrame({
    'name': ['John', 'Mary', 'Bob'],
    'age': [25, 28, 30],
    'city': ['New York', 'Paris', 'London']
})

# 제목
st.title('Chat GPT')

# 데이터 출력
st.write('Here is my data:')
st.write(data)

# 막대 그래프 출력
st.bar_chart(data['age'])
import streamlit as st

st.title('실습 예제')

import streamlit as st

# 제목 출력
st.title('실습 예제')

# selectbox 생성

option = st.selectbox(
    '원하는 항목을 선택하세요.',
     ('주차장', '도서관'))

# 선택된 값을 출력
st.write('당신은 "', option, '"을 선택했습니다.')

import streamlit as st

# 제목 출력
st.title('실습 테스트2')


import streamlit as st

# 제목 출력
st.title('실습 테스트2')

# 가로로 두 개의 열 생성
col1, col2 = st.columns(2)

# 첫 번째 열에는 "주차장" 출력
with col1:
    st.write("주차장")

# 두 번째 열에는 "도서관" 출력
with col2:
    st.write("도서관")

import streamlit as st
import requests
import pandas as pd

# 제목
st.title('신규 도서 정보')

# API 호출 및 데이터프레임 생성
url = 'http://openAPI.seoul.go.kr:8088/76796269766f756835305541427a6e/json/SeoulLibNewArrivalInfo/1/10/'
res = requests.get(url)
data = res.json()
df = pd.DataFrame(data['SeoulLibNewArrivalInfo']['row'])

# 데이터프레임 출력
st.write(df)

import streamlit as st
import requests
import pandas as pd

# 제목
st.title('실습 예제')

# Selectbox
options = ['주차장', '도서관']
choice = st.selectbox('데이터 선택', options)

# 선택한 데이터에 따라 데이터프레임 생성 및 출력
if choice == '주차장':
    url = 'http://openAPI.seoul.go.kr:8088/76796269766f756835305541427a6e/json/GetParkInfo/1/10/'
    res = requests.get(url)
    data = res.json()
    df = pd.DataFrame(data['GetParkInfo']['row'])
    st.write(df)
elif choice == '도서관':
    url = 'http://openAPI.seoul.go.kr:8088/76796269766f756835305541427a6e/json/SeoulLibNewArrivalInfo/1/10/'
    res = requests.get(url)
    data = res.json()
    df = pd.DataFrame(data['SeoulLibNewArrivalInfo']['row'])
    st.write(df)
