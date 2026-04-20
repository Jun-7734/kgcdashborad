import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. 페이지 설정 및 힙한 커스텀 CSS 적용
st.set_page_config(page_title="🎨 힙한 정관장 대시보드", layout="wide")

# 사이버펑크/네온 스타일 CSS
st.markdown("""
<style>
    /* 전체 배경 및 기본 글자색 */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    
    /* 네온 텍스트 타이틀 */
    .neon-title {
        font-size: 3.5rem !important;
        font-weight: 800;
        text-align: center;
        color: #fff;
        text-shadow: 
            0 0 7px #fff,
            0 0 10px #fff,
            0 0 21px #fff,
            0 0 42px #ff00de,
            0 0 82px #ff00de,
            0 0 92px #ff00de,
            0 0 102px #ff00de,
            0 0 151px #ff00de;
        margin-bottom: 0.5rem;
        letter-spacing: -2px;
    }
    
    .subtitle {
        text-align: center;
        color: #8b949e;
        font-size: 1.1rem;
        margin-bottom: 2.5rem;
    }

    /* 힙한 카드 스타일 */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 15px;
        padding: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        border-color: #ff00de;
    }

    /* Metric 글자색 커스텀 */
    div[data-testid="stMetricLabel"] {
        color: #8b949e !important;
        font-size: 1rem !important;
    }
    div[data-testid="stMetricValue"] {
        color: #0ae;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
    }

    /* Chart Container 스타일 */
    .chart-card {
        background: rgba(255, 255, 255, 0.02);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .chart-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #fff;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* 액션 아이템 스타일 */
    .action-item {
        background: linear-gradient(90deg, rgba(255, 0, 222, 0.1) 0%, rgba(138, 43, 226, 0.1) 100%);
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
        border-left: 4px solid #ff00de;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .action-icon {
        font-size: 1.5rem;
    }
    .action-text {
        color: #c9d1d9;
    }

    /* Streamlit 기본 요소 숨기기 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
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
        "local": [2400, 2300, 2200, 2100, 2000, 2500, 260
