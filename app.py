import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="🎩 프리미엄 다크 대시보드", layout="wide")

# 2. 구글 스프레드시트 주소 (사용자님 주소 연동)
GSHEET_URL = "https://docs.google.com/spreadsheets/d/1vCbyrVMsWOuVMTMWasIfW3-u9wJqCc-nAJn7C-WKQuo/export?format=csv"

@st.cache_data(ttl=60)
def load_gsheet_data():
    try:
        df = pd.read_csv(GSHEET_URL)
        df.columns = df.columns.str.strip().str.lower() 
        return df
    except Exception as e:
        return pd.DataFrame()

# 3. 선명한 가독성을 위한 다크 모드 스타일 설정
st.markdown("""
<style>
    /* 전체 배경: 아주 깊은 다크 네이비 */
    .stApp { 
        background-color: #0f172a; 
        color: #f8fafc; 
        font-family: 'Pretendard', sans-serif; 
    }
    
    /* 메인 타이틀: 선명한 실버-화이트 그라데이션 */
    .premium-title {
        font-size: 3.2rem !important; font-weight: 800; text-align: center;
        background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 2rem; letter-spacing: -1px;
    }
    
    /* 지표(Metric) 카드: 배경을 더 어둡게 하여 글씨가 돋보이게 함 */
    div[data-testid="stMetric"] {
        background: #1e293b !important; 
        border-radius: 24px;
        padding: 25px !important; 
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    
    /* 지표 제목(Label): 밝은 회색으로 가독성 확보 */
    div[data-testid="stMetricLabel"] { 
        color: #cbd5e1 !important; 
        font-weight: 600 !important; 
        font-size: 1.1rem !important; 
    }
    
    /* 지표 수치(Value): 선명한 코랄 레드 (가장 눈에 잘 띄는 색) */
    div[data-testid="stMetricValue"] { 
        color: #fb7185 !important; 
        font-weight: 800 !important; 
        font-size: 2.8rem !important; 
    }

    /* 차트 배경 카드 */
    .chart-card {
        background: #1e293b; 
        border-radius: 24px;
        padding: 30px; 
        border: 1px solid rgba(255, 255, 255, 0.05);
        margin-top: 10px;
    }
    
    .chart-header { color: #f8fafc; font-size: 1.3rem; font-weight: 700; margin-bottom: 15px; display: block; }
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

# --- 상단 지표 (IndentationError 완벽 해결) ---
if not df_metrics.empty and 'title' in df_metrics.columns:
    cols = st.columns(len(df_metrics))
    for i, row in df_metrics.iterrows():
        with cols[i]:
            # 이 줄의 들여쓰기가 매우 중요합니다.
            st.metric(label=str(row["title"]), value=str(row["value"]))
else:
    st.error("⚠️ 스프레드시트의 1행 제목을 'title'과 'value'로 정확히 수정해주세요.")

st.write("")

# --- 하단 차트 영역 ---
c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="chart-card"><b class="chart-header">📍 주간 판매 실적</b>', unsafe_allow_html=True)
    fig1 = px.bar(x=MARKETING_DATA["sales"]["labels"], y=MARKETING_DATA["sales"]["metro"], color_discrete_sequence=['#fb7185'])
    fig1.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#f8fafc", height=350,
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)')
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="chart-card"><b class="chart-header">📈 트렌드 분석</b>', unsafe_allow_html=True)
    fig2 = px.line(x=MARKETING_DATA["keywords"]["labels"], y=MARKETING_DATA["keywords"]["hiking"], color_discrete_sequence=['#818cf8'])
    fig2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#f8fafc", height=350,
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)')
    )
    fig2.update_traces(line=dict(width=4), mode='lines+markers')
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
