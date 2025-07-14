# 파일명: app.py
import streamlit as st

# MBTI별 추천 포켓몬 데이터
mbti_pokemon = {
    "ISTJ": ["블래키", "팬텀", "거북왕"],
    "ISFJ": ["이브이", "라프라스", "해피너스"],
    "INFJ": ["루기아", "세레비", "에브이"],
    "INTJ": ["뮤츠", "메타그로스", "야느와르몽"],
    "ISTP": ["리자몽", "마기라스", "핫삼"],
    "ISFP": ["피카츄", "푸린", "블래키"],
    "INFP": ["뮤", "마릴", "가디"],
    "INTP": ["프테라", "라티오스", "레어코일"],
    "ESTP": ["갸라도스", "던지미", "케켁킹"],
    "ESFP": ["피카츄", "푸크린", "닌탱굴"],
    "ENFP": ["에브이", "뮤", "치코리타"],
    "ENTP": ["팬텀", "드래펄트", "고래왕"],
    "ESTJ": ["거북왕", "렉쿄", "핫삼"],
    "ESFJ": ["해피너스", "이브이", "치코리타"],
    "ENFJ": ["라프라스", "루기아", "버터플"],
    "ENTJ": ["뮤츠", "드래펄트", "바리톱스"]
}

# 앱 제목
st.title("MBTI 포켓몬 추천기")

# 설명
st.write("당신의 MBTI에 가장 어울리는 포켓몬 3마리를 추천해드립니다!")

# MBTI 선택 박스
mbti = st.selectbox("MBTI를 선택하세요:", sorted(mbti_pokemon.keys()))

# 추천 결과 출력
if mbti:
    st.subheader(f"🧬 {mbti} 유형에게 추천하는 포켓몬:")
    for poke in mbti_pokemon[mbti]:
        st.write(f"- {poke}")
