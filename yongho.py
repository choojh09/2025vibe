import streamlit as st
import feedparser

# ✅ 뉴스 카테고리와 RSS URL 매핑 (정치 포함)
NEWS_SOURCES = {
    "IT/과학": "https://news.google.com/rss/headlines/section/technology?hl=ko&gl=KR&ceid=KR:ko",
    "사회": "https://news.google.com/rss/headlines/section/topic/NATION?hl=ko&gl=KR&ceid=KR:ko",
    "경제": "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=ko&gl=KR&ceid=KR:ko",
    "세계": "https://news.google.com/rss/headlines/section/topic/WORLD?hl=ko&gl=KR&ceid=KR:ko",
    "정치": "https://news.google.com/rss/headlines/section/topic/POLITICS?hl=ko&gl=KR&ceid=KR:ko"
}

# ✅ 페이지 설정
st.set_page_config(page_title="오늘의 뉴스 큐레이터", layout="centered")
st.title("🗞️ 오늘의 뉴스 큐레이터")
st.markdown("최신 뉴스 헤드라인을 카테고리별로 모아 보여드립니다.")

# ✅ 카테고리 선택
category = st.selectbox("뉴스 카테고리 선택", list(NEWS_SOURCES.keys()))
rss_url = NEWS_SOURCES[category]

# ✅ RSS 피드 파싱
feed = feedparser.parse(rss_url)

# ✅ 헤드라인 출력
st.subheader(f"📌 {category} 뉴스 헤드라인")

if feed.entries:
    for entry in feed.entries[:10]:
        st.markdown(f"### [{entry.title}]({entry.link})")
        if hasattr(entry, 'summary'):
            summary = entry.summary
            if len(summary) > 120:
                summary = summary[:120] + "..."
            st.caption(summary)
else:
    st.warning("😥 뉴스를 불러오지 못했습니다. 나중에 다시 시도해 주세요.")

st.markdown("---")
st.caption("뉴스 제공: Google News RSS | 제작: ChatGPT with Streamlit")
