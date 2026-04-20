import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="🎨 힙한 정관장 대시보드", layout="wide")

# 2. 스타일 설정
st.markdown("""
<style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .neon-title {
        font-size: 3rem !important; font-weight: 800; text-align: center; color: #fff;
        text-shadow: 0 0 10px #ff00de, 0 0 20px #ff00de; margin-bottom: 2rem;
    }
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03); border-radius: 15px;
        padding: 20px !important; border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .chart-card {
        background: rgba(255, 255, 255, 0.02); border-radius: 20px;
        padding: 25px; border: 1px solid rgba(255, 255, 255, 0.05); margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 3. 데이터 정의
MARKETING_DATA = {
    "stats": [
        {"title": "🚀 수도권 판매 성장", "value": "+15%"},
        {"title": "🎯 핵심 타겟 비중", "value": "45%"},
        {"title": "🔥 키워드 증가", "value": "+30%"},
        {"title": "⚠️ 지방 판매 추이", "value": "-2%"}
    ],
    "sales": {"labels": ['월', '화', '수', '목', '금', '토', '일'], "metro": [4000, 4500, 5200, 6100, 7500, 8200, 7800]},
    "keywords": {"labels": ['2월', '3월 1주', '3월 2주', '3월 3주', '3월 4주'], "hiking": [100, 110, 130, 160, 210]}
}

# 4. 레이아웃 구현
st.markdown('<h1 class="neon-title">EVERYTIME BALANCE</h1>', unsafe_allow_html=True)

# 상단 지표
cols = st.columns(4)
for i, stat in enumerate(MARKETING_DATA["stats"]):
    cols[i].metric(label=stat["title"], value=stat["value"])

st.write("")

# 중간 차트 영역 (에러 수정 지점)
c1, c2 = st.columns(2) # <-- 여기서 st.columns(2)라고 정확히 써야 합니다.

with c1:
    st.markdown('<div class="chart-card"><b>📍 판매량 현황</b>', unsafe_allow_html=True)
    fig1 = px.bar(x=MARKETING_DATA["sales"]["labels"], y=MARKETING_DATA["sales"]["metro"], color_discrete_sequence=['#ff00de'])
    fig1.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300)
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="chart-card"><b>📈 키워드 트렌드</b>', unsafe_allow_html=True)
    fig2 = px.line(x=MARKETING_DATA["keywords"]["labels"], y=MARKETING_DATA["keywords"]["hiking"], color_discrete_sequence=['#0ae'])
    fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white", height=300)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
