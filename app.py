import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="🎨 힙한 정관장 대시보드", layout="wide")

# 2. 구글 스프레드시트 주소 연동 (CSV 변환 주소)
GSHEET_URL = "https://docs.google.com/spreadsheets/d/1vCbyrVMsWOuVMTMWasIfW3-u9wJqCc-nAJn7C-WKQuo/export?format=csv"

@st.cache_data(ttl=60)
def load_gsheet_data():
    try:
        # 데이터 로드 및 헤더 공백 자동 제거
        df = pd.read_csv(GSHEET_URL)
        df.columns = df.columns.str.strip().str.lower() 
        return df
    except Exception as e:
        return pd.DataFrame()

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

# 4. 데이터 준비
df_metrics = load_gsheet_data()

MARKETING_DATA = {
    "sales": {"labels": ['월', '화', '수', '목', '금', '토', '일'], "metro": [4000, 4500, 5200, 6100, 7500, 8200, 7800]},
    "keywords": {"labels": ['2월', '3월 1주', '3월 2주', '3월 3주', '3월 4주'], "hiking": [100, 110, 130, 160, 210]}
}

# 5. 레이아웃 구현
st.markdown('<h1 class="neon-title">EVERYTIME BALANCE</h1>', unsafe_allow_html=True)

# --- 상단 지표 영역 ---
if not df_metrics.empty and 'title' in df_metrics.columns and 'value' in df_metrics.columns:
    cols = st.columns(len(df_metrics))
    for i, row in df_metrics.iterrows():
        with cols[i]:
            st.metric(label=str(row["title"]), value=str(row["value"]))
else:
    st.error("⚠️ 스프레드시트의 1행 제목을 'title'과 'value'로 정확히 수정해주세요.")

st.write("")

# --- 중간 차트 영역 ---
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
