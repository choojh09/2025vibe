import streamlit as st
import feedparser
import html

# ✅ 페이지 기본 설정
st.set_page_config(page_title="오늘의 뉴스 큐레이터", layout="wide")
st.title("🗞️ 오늘의 뉴스 큐레이터")

# ✅ 탭 나누기
tab1, tab2 = st.tabs(["📂 카테고리별 뉴스", "📰 언론사별 뉴스"])

# ✅ 뉴스 출력 함수
def render_news(feed_url):
    feed = feedparser.parse(feed_url)
    if feed.entries:
        for entry in feed.entries[:10]:
            title = html.unescape(entry.title)
            link = entry.link
            summary = html.unescape(entry.summary) if hasattr(entry, 'summary') else ""
            st.markdown(f"### [{title}]({link})")
            if summary:
                summary = summary.split("<")[0].strip()
                if len(summary) > 100:
                    summary = summary[:100] + "..."
                st.caption(summary)
    else:
        st.warning("❌ 뉴스를 불러올 수 없습니다.")

# ✅ 탭 1: 카테고리별 뉴스
with tab1:
    st.subheader("카테고리를 선택하세요")
    NEWS_CATEGORIES = {
        "종합": "https://news.google.com/rss/headlines/section/technology?hl=ko&gl=KR&ceid=KR:ko",
        "사회": "https://news.google.com/rss/headlines/section/topic/NATION?hl=ko&gl=KR&ceid=KR:ko",
        "경제": "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=ko&gl=KR&ceid=KR:ko",
        "세계": "https://news.google.com/rss/headlines/section/topic/WORLD?hl=ko&gl=KR&ceid=KR:ko",
        "정치": "https://news.google.com/rss/headlines/section/topic/POLITICS?hl=ko&gl=KR&ceid=KR:ko"
    }
    selected_category = st.selectbox("뉴스 카테고리 선택", list(NEWS_CATEGORIES.keys()))
    render_news(NEWS_CATEGORIES[selected_category])

# ✅ 탭 2: 언론사별 뉴스
with tab2:
    st.subheader("언론사를 선택하세요")
    PRESS_RSS = {
        "조선일보": "https://www.chosun.com/arc/outboundfeeds/rss/?outputType=xml",
        "중앙일보 (정치)": "https://www.joongang.co.kr/rss/news/politics.xml",
        "동아일보": "https://rss.donga.com/total.xml",
        "한겨레": "https://www.hani.co.kr/rss/",
        "경향신문": "https://www.khan.co.kr/rss/rssdata/total_news.xml",
        "연합뉴스": "https://www.yna.co.kr/rss/all.xml",
        "YTN": "https://www.ytn.co.kr/rss/news_rss.xml",
        "MBC": "https://imnews.imbc.com/rss/news.xml",
        "SBS": "https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=01",
        "KBS": "https://news.kbs.co.kr/rss/rss.xml",
        "한국경제": "https://www.hankyung.com/rss/news.xml"
    }
    selected_press = st.selectbox("언론사 선택", list(PRESS_RSS.keys()))
    render_news(PRESS_RSS[selected_press])

# ✅ 바닥글
st.markdown("---")
st.caption("뉴스 제공: 각 언론사 및 Google News RSS | 제작: ChatGPT with Streamlit")
