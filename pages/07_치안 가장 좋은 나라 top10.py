# app.py

import streamlit as st
import plotly.graph_objects as go

# 앱 제목
st.title("🌍 세계에서 치안이 가장 좋은 나라 Top 10")

# 설명
st.write("""
이 그래프는 **Global Peace Index (GPI)** 데이터를 기반으로 전 세계에서 치안이 가장 좋은 국가를 시각화한 것입니다.  
점수는 참고용으로 가공된 값이며, **높을수록 더 안전**한 국가입니다.
""")

# 국가 및 안전 점수 데이터 (이모지 포함)
countries = [
    "🇮🇸 아이슬란드", "🇩🇰 덴마크", "🇮🇪 아일랜드", "🇳🇿 뉴질랜드", "🇦🇹 오스트리아",
    "🇸🇬 싱가포르", "🇨🇭 스위스", "🇳🇴 노르웨이", "🇸🇮 슬로베니아", "🇫🇮 핀란드"
]
safety_scores = [95, 92, 90, 89, 88, 87, 85, 84, 83, 82]

# Plotly 막대그래프 생성
fig = go.Figure(
    data=go.Bar(
        x=countries,
        y=safety_scores,
        marker_color='mediumseagreen',
        text=safety_scores,
        textposition='auto'
    )
)

# 레이아웃 설정
fig.update_layout(
    title="🛡️ 치안이 가장 좋은 나라 (GPI 기반)",
    xaxis_title="국가",
    yaxis_title="안전 점수",
    template="plotly_white",
    xaxis_tickangle=-15
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
