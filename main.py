import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# 메뉴 데이터
menus = {
    "한식": ["김치찌개", "된장찌개", "비빔밥", "불고기", "제육볶음", "삼겹살", "갈비탕", "순두부찌개"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "마파두부", "깐풍기"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "덴푸라", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "리조또"],
    "기타": ["떡볶이", "샐러드", "샌드위치", "김밥", "컵라면", "토스트", "타코", "케밥"]
}

st.set_page_config(page_title="룰렛 점심 추천기", layout="centered")

st.title("🎡 오늘 뭐 먹지? 점심 룰렛")

# 카테고리 선택
selected_categories = st.multiselect(
    "🍽️ 먹고 싶은 음식 종류 선택",
    options=menus.keys(),
    default=list(menus.keys())
)

# 메뉴 구성
combined_menu = sum([menus[cat] for cat in selected_categories], [])
excluded_menu = st.multiselect("🙅‍♂️ 제외할 메뉴 선택", options=combined_menu)
final_menu = [m for m in combined_menu if m not in excluded_menu]

# 룰렛 함수
def draw_wheel(menu_list, selected_index):
    num_items = len(menu_list)
    angles = np.linspace(0, 2 * np.pi, num_items + 1)
    colors = plt.cm.tab20.colors

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    wedges = ax.bar(
        x=angles[:-1],
        height=[1] * num_items,
        width=2 * np.pi / num_items,
        bottom=0,
        color=[colors[i % len(colors)] for i in range(num_items)],
        edgecolor='white'
    )

    # 메뉴 이름 텍스트
    for i, wedge in enumerate(wedges):
        angle = (wedge.get_theta() + wedge.get_width() / 2)
        ax.text(
            angle,
            0.6,
            menu_list[i],
            rotation=np.degrees(angle),
            ha='center',
            va='center',
            fontsize=10,
            color='black'
        )

    # 가운데 화살표
    ax.annotate('▼', xy=(0, 1.2), fontsize=30, ha='center', va='center', color='red')

    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_ylim(0, 1.2)
    ax.axis('off')
    st.pyplot(fig)

# 추천 버튼
if st.button("🎰 룰렛 돌리기!"):
    if not final_menu:
        st.warning("메뉴가 없습니다. 카테고리 또는 제외 메뉴를 확인하세요.")
    else:
        selected = random.choice(final_menu)
        selected_index = final_menu.index(selected)

        draw_wheel(final_menu, selected_index)
        st.success(f"🎉 오늘의 추천 메뉴는 **{selected}** 입니다!")
        st.balloons()
