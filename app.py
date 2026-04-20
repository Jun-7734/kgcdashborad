import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="🥈 메탈릭 정관장 대시보드", layout="wide")

# 2. 구글 스프레드시트 주소 연동
GSHEET_URL = "https://docs.google.com/spreadsheets/d/1vCbyrVMsWOuVMTMWasIfW3-u9wJqCc-nAJn7C-WKQuo/export?format=csv"

@st.cache_data(ttl=60)
def load_gsheet_data():
    try:
        df = pd.read_csv(GSHEET_URL)
        df.columns = df.columns.str.strip().str.lower() 
        return df
    except Exception as e:
        return pd.DataFrame()

# 3. 메탈릭 스타일 설정 (Brushed Metal Theme)
st.markdown("""
<style>
    /* 전체 배경: 어두운 금속 질감 그라데이션 */
    .stApp { 
        background: radial-gradient(circle at top, #2c3e50 0%, #000000 100%);
        color: #e2e8f0; 
        font-family: 'Pretendard', sans-serif; 
    }
    
    /* 타이틀: 크롬 메탈 광택 효과 */
    .metal-title {
        font-size: 3.5rem !important; font-weight: 900; text-align: center;
        background: linear-gradient(to bottom, #ffffff 20%, #8e9eab 50%, #ffffff 80%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 2rem; letter-spacing: 2px;
        filter: drop-shadow(0 2px 5px rgba(0,0,0,0.5));
    }
    
    /* 지표(Metric) 카드: 알루미늄 판 느낌 */
    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #1e293b, #0f172a) !important; 
        border-radius: 12px;
        padding: 25px !important; 
        border: 1px solid #475569 !important; /* 실버 베젤 느낌 */
        box-shadow: inset 0 1px 1px rgba(255,255,255,0.1), 0 10px 20px rgba(0,0,0,0.5);
    }
    
    /* 지표 글자 색상 (고대비 화이트) */
    div[data-testid="stMetricLabel"] { 
        color: #94a3b8 !important; 
        font-weight: 600 !important; 
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    div[data-testid="stMetricValue"] { 
        color: #ffffff !important; 
        font-weight: 800 !important; 
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }

    /* 차트 영역 카드 */
    .chart-card {
        background: rgba(15, 23, 42, 0.8); 
        border-radius: 15px;
        padding: 30px; 
        border: 1px solid #334155;
        box-shadow: 0 15px 35px rgba(0,0,0,0.4);
        margin-top: 15px;
    }
    
    .chart-header { color: #f8fafc; font-size: 1.2rem; font-weight: 700; border-left: 4px solid #94a3b8; padding-left: 10px; }
</style>
""", unsafe_allow_html=True)

# 4. 데이터 로드
df_metrics = load_gsheet_data()

MARKETING_DATA = {
    "sales": {"labels": ['월', '화', '수', '목', '금', '토', '일'], "metro": [4000, 4500, 5200, 6100, 7500, 8200, 7800]},
    "keywords": {"labels": ['2월', '3월 1주', '3월 2주', '3월 3주', '3월 4주'], "hiking": [100, 110, 130, 160, 210]}
}

# 5. 레이아웃 구현
st.markdown('<h1 class="metal-title">EVERYTIME BALANCE</h1>', unsafe_allow_html=True)

# --- 지표 영역 ---
if not df_metrics.empty:
    cols = st.columns(len(df_metrics))
    for i, row in df_metrics.iterrows():
        with cols[i]:
            st.metric(label=str(row["title"]), value=str(row["value"]))
else:
    st.error("⚠️ 스프레드시트의 'title'과 'value'를 확인해주세요.")

st.write("")

# --- 차트 영역 (메탈 블루 & 실버 톤) ---
c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="chart-card"><b class="chart-header">WEEKLY PERFORMANCE</b>', unsafe_allow_html=True)
    # 쿨 그레이-블루 컬러 바
    fig1 = px.bar(x=MARKETING_DATA["sales"]["labels"], y=MARKETING_DATA["sales"]["metro"], color_discrete_sequence=['#64748b'])
    fig1.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#cbd5e1", height=350,
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)')
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="chart-card"><b class="chart-header">TREND ANALYSIS</b>', unsafe_allow_html=True)
    # 일렉트릭 블루 라인
    fig2 = px.line(x=MARKETING_DATA["keywords"]["labels"], y=MARKETING_DATA["keywords"]["hiking"], color_discrete_sequence=['#38bdf8'])
    fig2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#cbd5e1", height=350,
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)')
    )
    fig2.update_traces(line=dict(width=4), mode='lines+markers', marker=dict(size=8, color='white', line=dict(width=2, color='#38bdf8')))
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
