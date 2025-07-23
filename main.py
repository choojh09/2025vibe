import streamlit as st
import random
import time

# 음식 데이터 (더 추가 가능)
menus = {
    "한식": ["김치찌개", "된장찌개", "비빔밥", "불고기", "제육볶음", "삼겹살", "순두부찌개", "갈비탕", "국밥", "부대찌개"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "마파두부", "깐풍기", "볶음밥", "꿔바로우"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "덴푸라", "규동", "돈카츠", "오코노미야끼"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "리조또", "오믈렛", "그라탱"],
    "기타": ["샐러드", "샌드위치", "김밥", "컵라면", "떡볶이", "순대", "토스트", "타코", "케밥"]
}

st.title("🎡 오늘 뭐 먹지? 룰렛 점심 추천기")

# 카테고리 선택
selected_categories = st.multiselect(
    "먹고 싶은 음식 종류를 선택하세요 👇",
    options=list(menus.keys()),
    default=list(menus.keys())
)

# 추천 버튼
if st.button("🎰 룰렛 돌리기!"):
    if not selected_categories:
        st.warning("카테고리를 하나 이상 선택해주세요.")
    else:
        combined_menu = sum([menus[cat] for cat in selected_categories], [])
        if not combined_menu:
            st.warning("선택된 카테고리에 메뉴가 없습니다.")
        else:
            st.subheader("🍽️ 룰렛을 돌리는 중입니다...")
            slot = st.empty()

            spins = random.randint(30, 40)  # 총 회전 수

            for i in range(spins):
                pick = random.choice(combined_menu)
                slot.markdown(
                    f"<h1 style='text-align: center; color: {'red' if i == spins - 1 else 'gray'};'>{pick}</h1>",
                    unsafe_allow_html=True
                )
                time.sleep(0.05 + i * 0.02)  # 점점 느려짐

            st.success("🎉 오늘의 점심 메뉴가 정해졌습니다!")
            st.balloons()

st.markdown("---")
st.caption("만든이: ChatGPT | 점심 고민은 이제 끝!")
