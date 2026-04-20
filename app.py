import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="🥈 메탈릭 화이트 대시보드", layout="wide")

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

# 3. 화이트 텍스트 & 메탈릭 스타일 설정
st.markdown("""
<style>
    /* 전체 배경: 딥 차콜 & 블랙 (글씨가 가장 잘 보이는 배경) */
    .stApp { 
        background: #0a0a0a;
        color: #ffffff !important; 
        font-family: 'Pretendard', sans-serif; 
    }
    
    /* 타이틀: 강렬한 화이트 메탈 광택 */
    .metal-title {
        font-size: 3.5rem !important; font-weight: 900; text-align: center;
        color: #ffffff;
        text-shadow: 0 0 15px rgba(255, 255, 255, 0.5);
        margin-bottom: 2rem; letter-spacing: 2px;
    }
    
    /* 지표(Metric) 카드: 브러시드 실버 테두리 + 딥 블랙 배경 */
    div[data-testid="stMetric"] {
        background: #161616 !important; 
        border-radius: 12px;
        padding: 25px !important; 
        border: 2px solid #ffffff !important; /* 화이트 테두리로 강조 */
        box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }
    
    /* 모든 지표 글자: 화이트로 통일 */
    div[data-testid="stMetricLabel"] { 
        color: #ffffff !important; 
        font-weight: 600 !important; 
        font-size: 1.2rem !important;
        opacity: 0.9;
    }
    
    div[data-testid="stMetricValue"] { 
        color: #ffffff !important; 
        font-weight: 800 !important; 
        font-size: 3rem !important;
    }

    /* 차트 영역 카드 */
    .chart-card {
        background: #161616; 
        border-radius: 15px;
        padding: 30px; 
        border: 1px solid #333333;
        margin-top: 15px;
    }
    
    /* 차트 헤더 화이트 */
    .chart-header { 
        color: #ffffff !important; 
        font-size: 1.4rem; 
        font-weight: 700; 
        border-left: 5px solid #ffffff; 
        padding-left: 15px; 
    }
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
            # 수치와 제목 모두 화이트로 출력됩니다.
            st.metric(label=str(row["title"]), value=str(row["value"]))
else:
    st.error("⚠️ 스프레드시트 설정 확인이 필요합니다 (제목: title, value)")

st.write("")

# --- 차트 영역 (고대비 화이트 & 실버 톤) ---
c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="chart-card"><b class="chart-header">WEEKLY SALES</b>', unsafe_allow_html=True)
    # 바 차트: 선명한 화이트/실버 계열 사용
    fig1 = px.bar(x=MARKETING_DATA["sales"]["labels"], y=MARKETING_DATA["sales"]["metro"], color_discrete_sequence=['#ffffff'])
    fig1.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#ffffff", height=350,
        xaxis=dict(showgrid=False, tickfont=dict(color='white')),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)', tickfont=dict(color='white'))
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="chart-card"><b class="chart-header">TREND DATA</b>', unsafe_allow_html=True)
    # 라인 차트: 화이트 라인 + 굵은 마커
    fig2 = px.line(x=MARKETING_DATA["keywords"]["labels"], y=MARKETING_DATA["keywords"]["hiking"], color_discrete_sequence=['#ffffff'])
    fig2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#ffffff", height=350,
        xaxis=dict(showgrid=False, tickfont=dict(color='white')),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)', tickfont=dict(color='white'))
    )
    fig2.update_traces(line=dict(width=5), mode='lines+markers', marker=dict(size=10, color='white'))
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
