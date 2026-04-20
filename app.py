import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. 페이지 설정 및 커스텀 CSS 적용
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
        border: 1px solid rgba(255, 255, 255, 0.0
