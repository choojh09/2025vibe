import streamlit as st
import random
import time

# 다양한 음식 추가
menus = {
    "한식": [
        "김치찌개", "된장찌개", "비빔밥", "불고기", "제육볶음", "삼겹살", "순두부찌개",
        "갈비탕", "국밥", "육개장", "부대찌개", "콩나물국밥", "닭갈비", "돌솥비빔밥", "청국장"
    ],
    "중식": [
        "짜장면", "짬뽕", "탕수육", "마라탕", "마파두부", "깐풍기", "유산슬", "볶음밥",
        "양장피", "꿔바로우", "중식 덮밥"
    ],
    "일식": [
        "초밥", "라멘", "가츠동", "우동", "덴푸라", "규동", "야키소바", "오코노미야끼",
        "돈카츠", "냉모밀", "스시롤"
    ],
    "양식": [
        "파스타", "피자", "스테이크", "햄버거", "리조또", "치킨까스", "토마호크", "그라탱",
        "오믈렛", "로스트 치킨"
    ],
    "기타": [
        "샐러드", "샌드위치", "도시락", "컵라면", "김밥", "떡볶이", "순대", "핫도그", 
        "토스트", "포케", "타코", "케밥"
    ]
}

st.title("🤔 오늘 뭐 먹지?")
st.subheader("🍽️ 점심 메뉴 추천기")

# 카테고리 선택
selected_categories = st.multiselect(
    "먹고 싶은 음식 종류를 선택하세요:",
    options=list(menus.keys()),
    default=list(menus.keys())
)

# 추천 버튼
if st.button("🎯 메뉴 추천받기"):
    if not selected_categories:
        st.warning("카테고리를 최소 하나 이상 선택하세요.")
    else:
        # 선택된 메뉴 모으기
        combined_menu = sum([menus[cat] for cat in selected_categories], [])
        
        if not combined_menu:
            st.warning("선택한 카테고리에 메뉴가 없습니다.")
        else:
            st.subheader("🍀 추천 중입니다...")
            slot = st.empty()

            # 룰렛 애니메이션 (가짜 선택 효과)
            for i in range(20):
                option = random.choice(combined_menu)
                slot.markdown(f"<h2 style='text-align:center; color:gray'>{option}</h2>", unsafe_allow_html=True)
                time.sleep(0.1 + i*0.01)  # 점점 느려짐

            # 최종 추천
            final_pick = random.choice(combined_menu)
            slot.markdown(f"<h1 style='text-align:center; color:green'>🎉 오늘은 '{final_pick}' 어떠세요?</h1>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with ❤️ by ChatGPT")

