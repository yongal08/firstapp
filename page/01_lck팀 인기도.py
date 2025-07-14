# 파일명: app.py
import streamlit as st
import plotly.graph_objects as go

# 앱 제목
st.title("📊 LCK 팀 인기도 시각화")

# 설명
st.write("아래는 LCK 주요 팀들의 인기도(예시 수치 기준)를 막대그래프로 나타낸 것입니다.")

# LCK 팀과 인기도(예: 팬 투표 수 or 팬덤 지수) 데이터 - 예시 데이터
team_names = [
    "T1", "Gen.G", "Hanwha Life", "KT Rolster", "Dplus KIA",
    "DRX", "Kwangdong Freecs", "Nongshim RedForce", "OKSavingsBank BRION", "FearX"
]

popularity = [95000, 87000, 60000, 55000, 52000, 42000, 30000, 27000, 24000, 21000]

# Plotly 막대그래프 생성
fig = go.Figure(data=[
    go.Bar(
        x=team_names,
        y=popularity,
        marker_color='indianred'
    )
])

# 그래프 레이아웃 설정
fig.update_layout(
    title="LCK 팀별 인기도",
    xaxis_title="팀",
    yaxis_title="인기도 지수",
    template="plotly_white"
)

# Streamlit에 Plotly 그래프 표시
st.plotly_chart(fig)
