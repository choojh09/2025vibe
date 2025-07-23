import streamlit as st
import random

# 카테고리별 점심 메뉴
menus = {
    "한식": ["김치찌개", "불고기", "비빔밥", "제육볶음", "된장찌개", "삼겹살", "순두부찌개"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마파두부", "볶음밥"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "덴푸라"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "리조또"],
    "기타": ["샐러드", "분식", "샌드위치", "도시락", "컵라면"]
}

st.title("🤔 오늘 뭐 먹지? - 점심 메뉴 추천기")

# 카테고리 선택
st.subheader("🍱 먹고 싶은 음식 종류를 선택하세요")
selected_categories = st.multiselect(
    "카테고리 선택 (하나 이상 선택)",
    options=list(menus.keys()),
    default=list(menus.keys())
)

# 추천 버튼
if st.button("🍽 메뉴 추천받기"):
    if selected_categories:
        # 선택된 카테고리에서 메뉴 추출
        combined_menu = sum([menus[cat] for cat in selected_categories], [])
        if combined_menu:
            menu = random.choice(combined_menu)
            st.success(f"👉 오늘의 추천 메뉴는 **{menu}** 입니다!")
        else:
            st.warning("선택된 카테고리에 메뉴가 없습니다.")
    else:
        st.warning("카테고리를 한 개 이상 선택해주세요.")

# 하단 설명
st.markdown("---")
st.caption("메뉴 고민은 이제 그만! 🧠 만든이: ChatGPT")
