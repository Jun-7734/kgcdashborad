%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. 페이지 설정 및 힙한 커스텀 CSS 적용
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

    /* 힙한 카드 스타일 (Gradient Border) */
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
        border: 1px solid rgba(255, 255, 255, 0.05);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .chart-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #fff;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* 액션 아이템 스타일 */
    .action-item {
        background: linear-gradient(90deg, rgba(255, 0, 222, 0.1) 0%, rgba(138, 43, 226, 0.1) 100%);
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
        border-left: 4px solid #ff00de;
        display: flex;
        align-items: center;
        gap: 15px;
    }
    .action-icon {
        font-size: 1.5rem;
    }
    .action-text {
        color: #c9d1d9;
    }

    /* Streamlit 기본 요소 숨기기 (깔끔하게) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 2. 데이터 정의 (동일)
MARKETING_DATA = {
    "stats": [
        {"title": "🚀 수도권 판매 성장", "value": "+15%"},
        {"title": "🎯 핵심 타겟 비중", "value": "45%"},
        {"title": "🔥 액티브 키워드 증가", "value": "+30%"},
        {"title": "⚠️ 지방 판매 추이", "value": "-2%"}
    ],
    "sales": {
        "labels": ['월', '화', '수', '목', '금', '토', '일'],
        "metro": [4000, 4500, 5200, 6100, 7500, 8200, 7800],
        "local": [2400, 2300, 2200, 2100, 2000, 2500, 2600]
    },
    "keywords": {
        "labels": ['2월', '3월 1주', '3월 2주', '3월 3주', '3월 4주'],
        "hiking": [100, 110, 130, 160, 210],
        "tennis": [80, 95, 120, 150, 195]
    },
    "age_groups": {"labels": ['⚡️ 2030 사회초년생', '💼 40대 직장인', '🧓 50대 이상', '➕ 기타'], "values": [45, 25, 20, 10]},
    "actions": [
        {"icon": "🎁", "title": "편의점 채널 프로모션 최적화", "desc": "사회초년생의 반복 구매 습관 형성을 위한 2+1 및 모바일 바우처 증정"},
        {"icon": "🎾", "title": "'Active Lifestyle' 캠페인 가동", "desc": "#오운완 테니스/등산 커뮤니티 타겟 SNS 챌린지 및 인플루언서 협업"},
        {"icon": "💬", "title": "패키지 QC 강화 및 가격 심리 방어", "desc": "개봉 편의성 개선 및 대형마트용 실속형 대용량 패키지 기획"}
    ]
}

# 3. 레이아웃 구현

# 헤더 영역
st.markdown('<h1 class="neon-title">EVERYTIME BALANCE</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Marketing Performance Dashboard // KGC // 2026.04</p>', unsafe_allow_html=True)

# Stats Grid (상단 지표)
st.markdown('<div class="chart-card">', unsafe_allow_html=True)
cols = st.columns(4)
for i, stat in enumerate(MARKETING_DATA["stats"]):
    with cols[i]:
        st.metric(label=stat["title"], value=stat["value"])
st.markdown('</div>', unsafe_allow_html=True)

st.write("") # 간격 조절

# 메인 차트 영역
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">📍 판매량 현황</div>', unsafe_allow_html=True)
    df_sales = pd.DataFrame({'요일': MARKETING_DATA["sales"]["labels"], '수도권': MARKETING_DATA["sales"]["metro"], '지방': MARKETING_DATA["sales"]["local"]})
    fig_sales = px.bar(df_sales, x='요일', y=['수도권', '지방'], 
                       barmode='group',
                       color_discrete_map={'수도권': '#ff00de', '지방': '#0ae'}) # 네온 핑크 & 네온 민트
    fig_sales.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#c9d1d9",
                            xaxis_gridcolor="#333", yaxis_gridcolor="#333")
    st.plotly_chart(fig_sales, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">📈 키워드 트렌드</div>', unsafe_allow_html=True)
    df_key = pd.DataFrame({'기간': MARKETING_DATA["keywords"]["labels"], '등산': MARKETING_DATA["keywords"]["hiking"], '테니스': MARKETING_DATA["keywords"]["tennis"]})
    fig_key = px.line(df_key, x='기간', y=['등산', '테니스'],
                      color_discrete_map={'등산': '#ff9100', '테니스': '#0ae'},
                      render_mode='svg')
    fig_key.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#c9d1d9",
                          xaxis_gridcolor="#333", yaxis_gridcolor="#333")
    st.plotly_chart(fig_key, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 하단 영역 (연령 구성 & 액션 아이템)
col3, col4 = st.columns([1, 1.8])

with col3:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">👥 고객 연령 구성</div>', unsafe_allow_html=True)
    # 힙한 Donut 차트 색상 (Gradient 느낌)
    fig_age = px.pie(values=MARKETING_DATA["age_groups"]["values"], 
                     names=MARKETING_DATA["age_groups"]["labels"],
                     color_discrete_sequence=['#ff00de', '#8a2be2', '#0ae', '#333'], # Pink, Purple, Mint, Gray
                     hole=0.6)
    fig_age.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="#c9d1d9",
                          showlegend=True, legend=dict(orientation="v", yanchor="middle", y=0.5))
    st.plotly_chart(fig_age, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="chart-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown('<div class="chart-title">✅ 핵심 액션 아이템</div>', unsafe_allow_html=True)
    for action in MARKETING_DATA["actions"]:
        st.markdown(f'''
            <div class="action-item">
                <div class="action-icon">{action['icon']}</div>
                <div class="action-text">
                    <strong>{action['title']}</strong><br/>
                    <span style="font-size:0.9rem; color:#8b949e;">{action['desc']}</span>
                </div>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
