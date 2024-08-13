import streamlit as st
import requests
import json

# 제목 설정
st.title('문장 바이트 수 계산 및 맞춤법 검사기 📝')

# 검사할 문장 입력 받기
sentence = st.text_area('검사할 문장을 입력해 주세요!')

# 이름 입력 받기
name = st.text_input('이름을 입력해주세요!')

# 바이트 수 계산 함수
def calculate_byte_size(text):
    return len(text.encode('utf-8'))

# 맞춤법 검사 함수
def check_spelling(text):
    try:
        response = requests.post(
            "https://m.search.naver.com/p/csearch/ocontent/spellchecker.nhn",
            data={"_callback": "mycallback", "q": text},
        )
        if response.status_code == 200:
            result_text = response.text
            result_json = json.loads(result_text[result_text.find("mycallback(") + len("mycallback("):-2])
            return result_json['message']['result']['notag_html']
        else:
            return "맞춤법 검사 요청이 실패했습니다."
    except Exception as e:
        return f"맞춤법 검사 중 오류가 발생했습니다: {str(e)}"

# 버튼을 클릭하면 바이트 수 계산 및 맞춤법 검사 결과 출력
if st.button('검사하기'):
    if name and sentence:  # 이름과 문장이 입력되었는지 확인
        byte_size = calculate_byte_size(sentence)
        st.write(f"{name}님이 입력한 문장의 바이트 수는 {byte_size}입니다.")
        
        corrected_sentence = check_spelling(sentence)
        st.write("맞춤법 검사 결과:")
        st.write(corrected_sentence)
    else:
        st.write("이름과 검사할 문장을 입력해주세요.")
