import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. 페이지 설정
st.set_page_config(page_title="🎨 힙한 정관장 대시보드", layout="wide")

# 2. 데이터 로드 함수 (DB/CSV 연동)
@st.cache_data
def load_db_data():
    csv_file = "data.csv"
    # 파일이 없는 경우를 대비한 기본 데이터 정의
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
    else:
        # 파일이 없을 때 보여줄 기본값
        data = {
            "title": ["🚀 수도권 판매 성장", "🎯 핵심 타겟 비중", "🔥 키워드 증가", "⚠️ 지방 판매 추이"],
            "value": ["0%", "0%", "0%", "0%"]
        }
        df = pd.DataFrame(data)
    return df

# 3. 스타일 설정
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

# 4. 데이터 정의 (상단 지표는 DB에서, 차트 데이터는 기존 형식 유지)
df_metrics = load_db_data()

MARKETING_DATA = {
    "sales": {"labels": ['월', '화', '수', '목', '금', '토', '일'], "metro": [4000, 4500, 5200, 6100, 7500, 8200, 7800]},
    "keywords": {"labels": ['2월', '3월 1주', '3월 2주', '3월 3주', '3월 4주'], "hiking": [100, 110, 130, 160, 210]}
}

# 5. 레이아웃 구현
st.markdown('<h1 class="neon-title">EVERYTIME BALANCE</h1>', unsafe_allow_html=True)

# --- 상단 지표 영역 (DB 데이터 반영) ---
cols = st.columns(len(df_metrics))
for i, row in df_metrics.iterrows():
    with cols[i]:
        st.metric(label=row["title"], value=row["value"])

st.write("")

# 중간 차트 영역
c1, c2 = st.columns(2)

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
