import streamlit as st
import random
import time

# 카테고리별 음식 메뉴
menus = {
    "한식": ["김치찌개", "된장찌개", "비빔밥", "불고기", "제육볶음", "삼겹살", "갈비탕", "순두부찌개"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "마파두부", "깐풍기"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "덴푸라", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "리조또"],
    "기타": ["떡볶이", "샐러드", "샌드위치", "김밥", "컵라면", "토스트", "타코", "케밥"]
}

st.set_page_config(page_title="점심 뭐 먹지?", layout="centered")

st.title("🎯 오늘 뭐 먹지? 룰렛 점심 추천기")

# 1. 카테고리 선택
selected_categories = st.multiselect(
    "🍱 먹고 싶은 음식 종류를 선택하세요",
    options=list(menus.keys()),
    default=list(menus.keys())
)

# 2. 선택된 메뉴 목록
combined_menu = sum([menus[cat] for cat in selected_categories], [])

# 3. 제외할 메뉴 선택
excluded_items = st.multiselect(
    "🙅 제외할 메뉴를 선택하세요 (싫어하는 음식 등)",
    options=combined_menu
)

# 4. 최종 후보군
final_menu = [item for item in combined_menu if item not in excluded_items]

# 5. 룰렛 돌리기 버튼
if st.button("🎰 룰렛 돌리기!"):
    if not selected_categories:
        st.warning("카테고리를 하나 이상 선택해주세요.")
    elif not final_menu:
        st.warning("선택된 메뉴가 없습니다. 제외 메뉴를 확인해주세요.")
    else:
        st.subheader("🍽️ 추천 중...")
        slot = st.empty()

        spins = random.randint(25, 35)
        for i in range(spins):
            pick = random.choice(final_menu)
            slot.markdown(
                f"<h1 style='text-align: center; color: {'gray' if i < spins - 1 else 'green'}'>{pick}</h1>",
                unsafe_allow_html=True
            )
            time.sleep(0.05 + i * 0.02)  # 점점 느려짐

        st.success(f"🎉 오늘의 추천 메뉴는 **{pick}** 입니다!")
        st.balloons()

st.markdown("---")
st.caption("Made with ❤️ by ChatGPT")
