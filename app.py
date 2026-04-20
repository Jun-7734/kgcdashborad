import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. 페이지 설정 및 커스텀 CSS 적용
st.set_page_config(page_title="🎨 힙한 정관장 대시보드", layout="wide")

# 사이버펑크/네온 스타일 CSS
st.markdown("""
<style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .neon-title {
        font-size: 3.5rem !important;
        font-weight: 800;
        text-align: center;
        color: #fff;
        text-shadow: 0 0 7px #fff, 0 0 10px #fff, 0 0 21px #fff, 0 0 42px #ff00de, 0 0 82px #ff00de;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #8b949e;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
    }
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 15px;
        padding: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .chart-card {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .action-item {
        background: linear-gradient(90deg, rgba(255, 0, 222, 0.1) 0%, rgba(138, 43, 226, 0.1) 100%);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 10px;
        border-left: 4px solid #ff00de;
    }
</style>
""", unsafe_allow_html=True)

# 2. 데이터 정의
MARKETING_DATA = {
    "stats": [
        {"title": "🚀 수도권 판매 성장", "value": "+15%"},
        {"title": "🎯 핵심 타겟 비중", "value": "45%"},
        {"title": "🔥 액티브 키워드 증가", "value": "+30%"},
        {"title": "⚠️ 지방 판매 추이", "value": "-2%"}
    ],
    "sales": {
        "labels": ['월', '화', '수', '목', '금', '토', '일'],
        "metro": [4000, 4500, 5200, 6100, 7500, 8200, 7800],
        "local": [2400, 2300, 2200, 2100, 2000, 2500, 2600]
    },
    "keywords": {
        "labels": ['2월', '3월 1주', '3월 2주', '3월 3주', '3월 4주'],
        "hiking": [100, 110, 130, 160, 210],
        "tennis": [80, 95, 120, 150, 195]
    },
    "age_groups": {"labels": ['⚡️ 2030', '💼 40대', '🧓 50대', '➕ 기타'], "values": [45, 25, 20, 10]},
    "actions": [
        {"icon": "🎁", "title": "편의점 프로모션", "desc": "2+1 및 모바일 바우처 증정"},
        {"icon": "🎾", "title": "액티브 캠페인", "desc": "테니스/등산 SNS 챌린지"},
        {"icon": "💬", "title": "패키지 개선", "desc": "실속형 대용량 패키지 기획"}
    ]
}

# 3. 레이아웃 구현
st.markdown('<h1 class="neon-title">EVERYTIME BALANCE</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Marketing Performance Dashboard // KGC // 2026</p>', unsafe_allow_html=True)

# 상단 지표
cols = st.columns(4)
for i, stat in enumerate(MARKETING_DATA["stats"]):
    cols[i].metric(label=stat["title"], value=stat["value"])

# 차트 영역
c1, c2 = st
