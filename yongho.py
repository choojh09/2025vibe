import streamlit as st
import feedparser

# 뉴스 카테고리와 RSS URL 매핑
NEWS_SOURCES = {
    "IT/과학": "https://news.google.com/rss/headlines/section/technology?hl=ko&gl=KR&ceid=KR:ko",
    "사회": "https://news.google.com/rss/headlines/section/topic/NATION?hl=ko&gl=KR&ceid=KR:ko",
    "경제": "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=ko&gl=KR&ceid=KR:ko",
    "세계": "https://news.google.com/rss/headlines/section/topic/WORLD?hl=ko&gl=KR&ceid=KR:ko"
}

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 뉴스 큐레이터", layout="centered")
st.title("🗞️ 오늘의 뉴스 큐레이터")
st.markdown("최신 뉴스 헤드라인을 모아 보여드립니다.")

# 카테고리 선택
category = st.selectbox("뉴스 카테고리 선택", list(NEWS_SOURCES.keys()))
rss_url = NEWS_SOURCES[category]

# 뉴스 가져오기
feed = feedparser.parse(rss_url)

# 헤드라인 출력
st.subheader(f"📌 {category} 뉴스 헤드라인")
for entry in feed.entries[:10]:
    st.markdown(f"### [{entry.title}]({entry.link})")
    if hasattr(entry, 'summary'):
        st.caption(entry.summary[:100] + "..." if len(entry.summary) > 100 else entry.summary)

st.markdown("---")
st.caption("뉴스 제공: Google News RSS | 제작: ChatGPT")
