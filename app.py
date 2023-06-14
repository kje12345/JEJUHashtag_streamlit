import streamlit as st
import pandas as pd


df = pd.read_csv("음식점_해시태그.csv", sep=",")

keyword1 = st.text_input("제주도 어디로 여행가시나요? ex)제주시, 서귀포시")
keyword2 = st.text_input("출출한데 밥부터 먹고 시작해요. 먹고 싶은 거 있어요? ex)회, 흑돼지")
keyword3 = st.text_input("밥 먹으면서 어떤 경치를 즐길까요? ex) 바다, 한라산")
result = []

if keyword1 and keyword2 and keyword3:
    for i in range(len(df)):
        if keyword1 in str(df['해시태그'][i]) and keyword2 in str(df['해시태그'][i]) and keyword3 in str(df['해시태그'][i]):
            result.append(df['명칭'][i])
                
        if len(result) == 0:
        result.append("결과가 존재하지 않습니다. 해시태그를 아래질문부터 수정해 보세요.")

for r in result:
    st.title(r)
