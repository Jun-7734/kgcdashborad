import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="🥈 화이트 메탈 대시보드", layout="wide")

# 2. 구글 스프레드시트 주소 연동 (사용자님 시트 주소)
GSHEET_URL = "https://docs.google.com/spreadsheets/d/1vCbyrVMsWOuVMTMWasIfW3-u9wJqCc-nAJn7C-WKQuo/export?format=csv"

@st.cache_data(ttl=60)
def load_gsheet_data():
    try:
        df = pd.read_csv(GSHEET_URL)
        df.columns = df.columns.str.strip().str.lower() 
        return df
    except Exception as e:
        # 데이터 로드 실패 시 표시할 기본 데이터
        return pd.DataFrame({
            "title": ["🚀 수도권 판매 성장", "🎯 핵심 타겟 비중", "🔥 키워드 증가", "⚠️ 지방 판매 추이"],
            "value": ["50%", "78%", "+120%", "-15%"]
        })

# 3. 고대비 메탈릭 스타일 설정 (모든 텍스트 화이트)
st.markdown("""
<style>
    /* 전체 배경: 블랙에 가까운 다크 네이비 */
    .stApp { 
        background-color: #05070a; 
        color: #ffffff !important; 
        font-family: 'Pretendard', sans-serif; 
    }
    
    /* 타이틀: 실버 광택 화이트 */
    .metal-title {
        font-size: 3.5rem !important; font-weight: 900; text-align: center;
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.4);
        margin-bottom: 2.5rem;
    }
    
    /* 지표(Metric) 카드: 화이트 테두리로 시인성 극대화 */
    div[data-testid="stMetric"] {
        background: #111827 !important; 
        border-radius: 12px;
        padding: 25px !important; 
        border: 2px solid #ffffff !important; /* 굵은 화이트 테두리 */
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    
    /* 모든 지표 텍스트를 순백색으로 고정 */
    div[data-testid="stMetricLabel"] { 
        color: #ffffff !important; 
        font-weight: 700 !important; 
        font-size: 1.2rem !important;
        opacity: 1.0 !important;
    }
    
    div[data-testid="stMetricValue"] { 
        color: #ffffff !important; 
        font-weight: 900 !important; 
        font-size: 3.2rem !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    }

    /* 차트 카드 디자인 */
    .chart-card {
        background: #111827; 
        border-radius: 15px;
        padding: 30px; 
        border: 1px solid #334155;
        margin-top: 15px;
    }
    
    .chart-header { 
        color: #ffffff !important; 
        font-size: 1.4rem; 
        font-weight: 700; 
        border-left: 6px solid #ffffff; 
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

# --- 지표 영역 (화이트 텍스트 강조) ---
if not df_metrics.empty:
    cols = st.columns(len(df_metrics))
    for i, row in df_metrics.iterrows():
        with cols[i]:
            # 데이터 수치와 제목 모두 화이트로 표시됩니다.
            st.metric(label=str(row["title"]), value=str(row["value"]))
else:
    st.error("⚠️ 스프레드시트의 1행 제목이 'title', 'value'인지 확인해주세요.")

st.write("")

# --- 차트 영역 ---
c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="chart-card"><b class="chart-header">WEEKLY PERFORMANCE</b>', unsafe_allow_html=True)
    # 차트 바 색상도 밝은 실버/화이트 계열로 설정
    fig1 = px.bar(x=MARKETING_DATA["sales"]["labels"], y=MARKETING_DATA["sales"]["metro"], color_discrete_sequence=['#f8fafc'])
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
    # 라인 차트는 선명한 화이트 라인 사용
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
