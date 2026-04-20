import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 페이지 설정
st.set_page_config(page_title="🎨 트렌디 정관장 대시보드", layout="wide")

# 2. 구글 스프레드시트 주소 연동 (CSV 변환 주소) - 사용자님의 주소 유지
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

# 3. 새로운 스타일 설정 (밝고 힙한 스타일)
st.markdown("""
<style>
    /* 전체 배경색: 매우 밝은 회색 (쾌적하고 세련된 느낌) */
    .stApp { background-color: #f8f9fa; color: #333; font-family: 'Pretendard', sans-serif; }
    
    /* 타이틀 스타일: 보드하고 깔끔한 Gradient (매거진 같은 느낌) */
    .trendy-title {
        font-size: 3.5rem !important; font-weight: 900; text-align: center;
        background: linear-gradient(135deg, #ff6b6b 0%, #4da6ff 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 2.5rem; letter-spacing: -2px;
    }
    
    /* 지표(Metric) 카드 스타일: 흰색 배경 + 부드러운 그림자 (세련된 가구 같은 느낌) */
    div[data-testid="stMetric"] {
        background: #ffffff; border-radius: 20px;
        padding: 25px !important; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03); 
        border: 1px solid rgba(0, 0, 0, 0.01);
        transition: transform 0.2s ease-in-out;
    }
    div[data-testid="stMetric"]:hover { transform: translateY(-5px); }
    
    /* 지표 라벨과 값 색상 */
    div[data-testid="stMetricLabel"] { color: #1a2a4e !important; font-weight: 700; font-size: 1.1rem !important; }
    div[data-testid="stMetricValue"] { color: #ff6b6b !important; font-weight: 800; font-size: 2.8rem !important; }

    /* 차트 카드 스타일: Metric 카드와 동일한 스타일 적용 */
    .chart-card {
        background: #ffffff; border-radius: 20px;
        padding: 30px; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);
        margin-top: 15px;
    }
    
    /* 차트 제목 스타일 */
    .chart-title { color: #1a2a4e; font-size: 1.3rem; font-weight: 700; margin-bottom: 1rem; display: block;}
    
    /* 폰트 설정 (Pretendard 권장, 없을 경우 기본 sans-serif) */
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
</style>
""", unsafe_allow_html=True)

# 4. 데이터 준비
df_metrics = load_gsheet_data()

MARKETING_DATA = {
    "sales": {"labels": ['월', '화', '수', '목', '금', '토', '일'], "metro": [4000, 4500, 5200, 6100, 7500, 8200, 7800]},
    "keywords": {"labels": ['2월', '3월 1주', '3월 2주', '3월 3주', '3월 4주'], "hiking": [100, 110, 130, 160, 210]}
}

# 5. 레이아웃 구현
# 잘려있던 제목 부분을 새로운 그라데이션 타이틀로 변경
st.markdown('<h1 class="trendy-title">EVERYTIME BALANCE</h1>', unsafe_allow_html=True)

# --- 상단 지표 영역 (구글 시트 연동) ---
if not df_metrics.empty and 'title' in df_metrics.columns and 'value' in df_metrics.columns:
    cols = st.columns(len(df_metrics))
    for i, row in df_metrics.iterrows():
        with cols[i]:
            # Metric 컴포넌트를 사용하여 카드 출력
            st.metric(label=str(row["title"]), value=str(row["value"]))
else:
    # 에러 메시지 스타일도 밝게 변경
    st.error("⚠️ 스프레드시트의 1행 제목을 'title'과 'value'로 정확히 수정해주세요.")

st.write("")

# --- 중간 차트 영역 (밝은 배경에 맞는 컬러로 변경) ---
c1, c2 = st.columns(2)

with c1:
    st.markdown('<div class="chart-card"><b class="chart-title">📍 판매량 현황</b>', unsafe_allow_html=True)
    
    # 바 차트: 피치 코랄(#ff6b6b) 컬러 사용
    fig1 = px.bar(x=MARKETING_DATA["sales"]["labels"], y=MARKETING_DATA["sales"]["metro"], color_discrete_sequence=['#ff6b6b'])
    
    # 차트 레이아웃 수정: 흰색 배경, 회색 글자, 연한 그리드
    fig1.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#666", height=350,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(showgrid=False), # X축 그리드 제거
        yaxis=dict(gridcolor='rgba(0,0,0,0.05)') # Y축 그리드 연하게
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="chart-card"><b class="chart-title">📈 키워드 트렌드</b>', unsafe_allow_html=True)
    
    # 라인 차트: 티파니 블루(#4da6ff) 컬러 사용 + 선 굵게
    fig2 = px.line(x=MARKETING_DATA["keywords"]["labels"], y=MARKETING_DATA["keywords"]["hiking"], color_discrete_sequence=['#4da6ff'])
    
    # 차트 레이아웃 수정
    fig2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        font_color="#666", height=350,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor='rgba(0,0,0,0.05)')
    )
    # 선 스타일 수정 (더 굵고 부드럽게)
    fig2.update_traces(line=dict(width=4))
    
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
