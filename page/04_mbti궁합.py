# app.py

import streamlit as st

# MBTI별 잘 맞는 궁합 유형 (예시 데이터)
mbti_compatibility = {
    "ISTJ": ["ESFP", "ISFJ", "ESTJ"],
    "ISFJ": ["ESTP", "ISTJ", "ESFJ"],
    "INFJ": ["ENFP", "INTP", "ENFJ"],
    "INTJ": ["ENFP", "ENTP", "INFJ"],
    "ISTP": ["ESFJ", "ISFP", "ESTP"],
    "ISFP": ["ESFP", "ISFJ", "INFP"],
    "INFP": ["ENFJ", "INFJ", "ISFP"],
    "INTP": ["ENTP", "INTJ", "INFP"],
    "ESTP": ["ISFJ", "ESFP", "ISTP"],
    "ESFP": ["ISTJ", "ISFP", "ESTP"],
    "ENFP": ["INFJ", "INTJ", "INFP"],
    "ENTP": ["INFJ", "INTP", "ENFP"],
    "ESTJ": ["ISFJ", "ESFJ", "ISTJ"],
    "ESFJ": ["ISFP", "ESTJ", "ENFP"],
    "ENFJ": ["INFP", "INFJ", "ISFJ"],
    "ENTJ": ["INTP", "ENFP", "INTJ"]
}

# 앱 제목
st.title("💞 MBTI 궁합 추천기")

# 설명
st.write("당신의 MBTI와 궁합이 잘 맞는 MBTI 유형을 추천해드립니다!")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요:", sorted(mbti_compatibility.keys()))

# 결과 출력
if mbti:
    st.subheader(f"🔗 {mbti}와 궁합이 좋은 MBTI 유형:")
    for match in mbti_compatibility[mbti]:
        st.write(f"- {match}")
