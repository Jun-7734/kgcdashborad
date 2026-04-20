import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="🎩 프리미엄 정관장 대시보드", layout="wide")

# 2. 구글 스프레드시트 주소 연동 (사용자님 주소 유지)
GSHEET_URL = "https://docs.google.com/spreadsheets/d/1vCbyrVMsWOuVMTMWasIfW3-u9wJqCc-nAJn7C-WKQuo/export?format=csv"

@st.cache_data(ttl=60)
def load_gsheet_data():
    try:
        df = pd.read_csv(GSHEET_URL)
        df.columns = df.columns.str.strip().str.lower() 
        return df
    except Exception as e:
        return pd.DataFrame()

# 3. 프리미엄 다크 스타일 설정 (Apple 스타일 다크모드)
st.markdown("""
<style>
    /* 전체 배경: 깊은 밤의 다크 네이비 */
    .stApp { 
        background-color: #0f172a; 
        color: #f1f5f9; 
        font-family: 'Pretendard', sans-serif; 
    }
    
    /* 타이틀: 은은한 메탈릭 실버 그라데이션 */
    .premium-title {
        font-size: 3.2rem !important; font-weight: 800; text-align: center;
        background: linear-gradient(180deg, #ffffff 0%, #94a3b8 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 2rem; letter-spacing: -1.5px;
    }
    
    /* 카드 디자인: 유리 질감 효과 */
    div[data-testid="stMetric"] {
        background: rgba(30, 41, 59, 0.7); 
        border-radius: 20px;
        padding: 25px !important; 
        border: 1px solid rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
    }
    
    /* 지표 텍스트 컬러 */
    div[data-testid="stMetricLabel"] { color: #94a3b8 !important; font-weight: 500; font-size: 1rem !important; }
    div[data-testid="stMetricValue"] { color: #f87171 !important; font-weight: 700; font-size: 2.5rem !important; }

    /* 차트 카드 디자인 */
    .chart-card {
        background: rgba(30, 41, 59, 0.5); 
        border-radius: 24px;
        padding: 30px; 
        border: 1px solid rgba(255, 255, 255, 0.03);
        margin-top: 10px;
    }
    
    .chart-header { color: #f1f5f9; font-size: 1.2rem; font-weight: 600; margin-bottom: 15px; display: block; }
</style>
""", unsafe_allow_html=True)

# 4. 데이터 로드 및 정의
df_metrics = load_gsheet_data()

MARKETING_DATA = {
    "sales": {"labels": ['월', '화', '수', '목', '금', '토', '일'], "metro": [4000, 4500, 5200, 6100, 7500, 8200, 7800]},
    "keywords": {"labels": ['2월', '3월 1주', '3월 2주', '3월 3주', '3월 4주'], "hiking": [100, 110, 130, 160, 210]}
}

# 5. 레이아웃 구현
st.markdown('<h1 class="premium-title">EVERYTIME BALANCE</h1>', unsafe_allow_html=True)

# --- 상단 지표 (구글 시트 연동) ---
if not df_metrics.empty and 'title' in df_metrics.columns:
    cols = st.columns(len(df_metrics))
    for i, row in df_metrics.iterrows():
        with cols[i]:
            st.metric(label=str(row["title"]), value=str(row["value"]))
else:
    st.info("💡 스프레드시트 데이터를 기다리고 있습니다.")

st.write("")

# --- 하단 차트 (고급스러운 톤으로 조정) ---
c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="chart-card"><b class="chart-header">📍 주간 판매 실적</b>', unsafe_allow_html=True)
    # 정관장의 상징인 로즈 레드 컬러 적용
    fig1 = px.bar(x=MARKETING_DATA["sales"]["labels"], y=MARKETING_DATA["sales"]["metro"], color_discrete_sequence=['#f87171'])
    fig1.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#94a3b8", height=350,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)')
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="chart-card"><b class="chart-header">📈 트렌드 분석</b>', unsafe_allow_html=True)
    # 신뢰감을 주는 슬레이트 블루 컬러 적용
    fig2 = px.line(x=MARKETING_DATA["keywords"]["labels"], y=MARKETING_DATA["keywords"]["hiking"], color_discrete_sequence=['#818cf8'])
    fig2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#94a3b8", height=350,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)')
    )
    fig2.update_traces(line=dict(width=3), mode='lines+markers') # 선 굵기와 마커 추가
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
