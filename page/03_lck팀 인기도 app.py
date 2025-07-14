# app.py

import streamlit as st
import plotly.graph_objects as go

# 앱 제목
st.title("📊 LCK 팀 인기도 시각화")

# 팀과 인기도 점수 (예시 데이터)
team_names = [
    "T1", "Gen.G", "Hanwha Life", "KT Rolster", "Dplus KIA",
    "DRX", "Kwangdong Freecs", "Nongshim RedForce", "OKSavingsBank BRION", "FearX"
]
popularity = [95000, 87000, 60000, 55000, 52000, 42000, 30000, 27000, 24000, 21000]

# Plotly 막대 그래프 만들기
fig = go.Figure(
    data=go.Bar(x=team_names, y=popularity, marker_color='lightskyblue')
)

fig.update_layout(
    title="LCK 팀별 인기도 순위 (예시)",
    xaxis_title="팀 이름",
    yaxis_title="인기도 지수",
    template="simple_white"
)

# Plotly 차트 출력
st.plotly_chart(fig, use_container_width=True)
