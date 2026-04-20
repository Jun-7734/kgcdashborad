import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="🎨 힙한 정관장 대시보드", layout="wide")

# 2. 구글 스프레드시트 연동 설정
# 여기에 변환한 구글 시트 주소를 넣으세요.
GSHEET_URL = "https://docs.google.com/spreadsheets/d/ID값/export?format=csv"

@st.cache_data(ttl=60) # 60초마다 시트의 최신 데이터를 확인합니다.
def load_gsheet_data():
    try:
        # 온라인 상의 구글 시트를 데이터프레임으로 읽어옵니다.
        df = pd.read_csv(GSHEET_URL)
        return df
    except Exception as e:
        # 시트를 불러오지 못했을 때의 기본값
        st.warning("스프레드시트를 불러올 수 없어 기본값을 표시합니다.")
        data = {
            "title": ["🚀 수도권 판매 성장", "🎯 핵심 타겟 비중", "🔥 키워드 증가", "⚠️ 지방 판매 추이"],
            "value": ["-", "-", "-", "-"]
        }
        return pd.DataFrame(data)

# 3. 스타일 설정 (기존과 동일)
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

# 4. 데이터 로드 및 정의
df_metrics = load_gsheet_data()

MARKETING_DATA = {
    "sales": {"labels": ['월', '화', '수', '목', '금', '토', '일'], "metro": [4000, 4500, 5200, 6100, 7500, 8200, 7800]},
    "keywords": {"labels": ['2월', '3월 1주', '3월 2주', '3월 3주', '3월 4주'], "hiking": [100, 110, 130, 160, 210]}
}

# 5. 레이아웃 구현
st.markdown('<h1 class="neon-title">EVERYTIME BALANCE</h1>', unsafe_allow_html=True)

# --- 상단 지표 영역 (구글 시트 데이터 반영) ---
if not df_metrics.empty:
    cols = st.columns(len(df_metrics))
    for i, row in df_metrics.iterrows():
        with cols[i]:
