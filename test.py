import streamlit as st

user_name = st.text_input("당신의 이름을 입력하세요:")	# 입력 박스
if st.button("확인"):                                 	# "확인" 버튼을 누르면
    st.write("안녕하세요, "+user_name+"님!")           	# 특정 텍스트 출력