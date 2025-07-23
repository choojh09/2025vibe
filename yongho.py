import streamlit as st
import feedparser
import html

# ✅ 뉴스 카테고리와 RSS URL 매핑 (정치 포함)
NEWS_SOURCES = {
    "종합": "https://news.google.com/rss/headlines/section/technology?hl=ko&gl=KR&ceid=KR:ko",
    "사회": "https://news.google.com/rss/headlines/section/topic/NATION?hl=ko&gl=KR&ceid=KR:ko",
    "경제": "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=ko&gl=KR&ceid=KR:ko",
    "세계": "https://news.google.com/rss/headlines/section/topic/WORLD?hl=ko&gl=KR&ceid=KR:ko",
    "정치": "https://news.google.com/rss/headlines/section/topic/POLITICS?hl=ko&gl=KR&ceid=KR:ko"
}

# ✅ 페이지 설정
st.set_page_config(page_title="오늘의 뉴스 큐레이터", layout="centered")
st.title("🗞️ 오늘의 뉴스 큐레이터")
st.markdown("최신 뉴스 제목과 간단 요약을 카테고리별로 확인해보세요.")

# ✅ 카테고리 선택
category = st.selectbox("뉴스 카테고리 선택", list(NEWS_SOURCES.keys()))
rss_url = NEWS_SOURCES[category]

# ✅ RSS 파싱
feed = feedparser.parse(rss_url)

# ✅ 뉴스 출력
st.subheader(f"📌 {category} 뉴스 헤드라인")

if feed.entries:
    for entry in feed.entries[:10]:
        title = html.unescape(entry.title)
        link = entry.link
        summary = html.unescape(entry.summary) if hasattr(entry, 'summary') else ""

        st.markdown(f"### [{title}]({link})")
        if summary:
            # 간단한 요약 (HTML 태그 제거 및 길이 제한)
            clean_summary = summary.split("<")[0]  # HTML 태그 제거 대충 처리
            short_summary = clean_summary.strip()
            if len(short_summary) > 100:
                short_summary = short_summary[:100] + "..."
            st.caption(short_summary)
else:
    st.warning("😥 뉴스를 불러올 수 없습니다. 나중에 다시 시도해 주세요.")

st.markdown("---")
st.caption("뉴스 제공: Google News RSS | 제작: ChatGPT with Streamlit")
