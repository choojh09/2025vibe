import streamlit as st
import random
import json

st.set_page_config(page_title="점심 룰렛", layout="centered")

st.title("🎡 오늘 뭐 먹지? 점심 룰렛")

# 메뉴 카테고리
menus = {
    "한식": ["김치찌개", "된장찌개", "불고기", "비빔밥", "제육볶음", "삼겹살", "갈비탕", "순두부찌개"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "마파두부", "깐풍기"],
    "일식": ["초밥", "라멘", "가츠동", "우동", "덴푸라", "규동"],
    "양식": ["파스타", "피자", "스테이크", "햄버거", "리조또"],
    "기타": ["떡볶이", "샐러드", "샌드위치", "김밥", "컵라면", "토스트", "타코", "케밥"]
}

# 사용자 선택
selected_categories = st.multiselect(
    "🍱 먹고 싶은 음식 종류를 선택하세요",
    options=list(menus.keys()),
    default=list(menus.keys())
)

# 선택된 음식 리스트 만들기
combined_menu = sum([menus[cat] for cat in selected_categories], [])

if not combined_menu:
    st.warning("카테고리를 하나 이상 선택해주세요.")
else:
    # 메뉴 JSON으로 전달
    items_json = json.dumps(combined_menu)

    # 룰렛 UI 삽입
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center; margin-top: 30px;">
            <iframe srcdoc='
                <html>
                <head>
                    <style>
                        body {{ margin: 0; padding: 0; background: white; }}
                        canvas {{ display: block; margin: auto; }}
                        #spinButton {{
                            display: block;
                            margin: 20px auto;
                            padding: 10px 20px;
                            font-size: 18px;
                            background-color: #4CAF50;
                            color: white;
                            border: none;
                            border-radius: 5px;
                            cursor: pointer;
                        }}
                    </style>
                </head>
                <body>
                    <canvas id="wheel" width="400" height="400"></canvas>
                    <button id="spinButton">🎰 돌리기</button>
                    <script>
                        const items = {items_json};
                        const canvas = document.getElementById("wheel");
                        const ctx = canvas.getContext("2d");
                        const size = canvas.width;
                        const radius = size / 2;
                        const centerX = size / 2;
                        const centerY = size / 2;
                        let angle = 0;
                        let isSpinning = false;

                        function drawWheel() {{
                            const anglePerItem = 2 * Math.PI / items.length;
                            for (let i = 0; i < items.length; i++) {{
                                ctx.beginPath();
                                ctx.moveTo(centerX, centerY);
                                ctx.fillStyle = `hsl(${{i * 360 / items.length}}, 70%, 70%)`;
                                ctx.arc(centerX, centerY, radius, anglePerItem * i, anglePerItem * (i + 1));
                                ctx.fill();
                                ctx.save();
                                ctx.translate(centerX, centerY);
                                ctx.rotate(anglePerItem * (i + 0.5));
                                ctx.textAlign = "right";
                                ctx.fillStyle = "black";
                                ctx.font = "16px sans-serif";
                                ctx.fillText(items[i], radius - 10, 5);
                                ctx.restore();
                            }}
                        }}

                        function spinWheel() {{
                            if (isSpinning) return;
                            isSpinning = true;
                            let velocity = Math.random() * 0.3 + 0.25;
                            let deceleration = 0.002;
                            const spin = setInterval(() => {{
                                angle += velocity;
                                velocity -= deceleration;
                                if (velocity <= 0) {{
                                    clearInterval(spin);
                                    angle %= 2 * Math.PI;
                                    const selectedIndex = Math.floor(items.length - (angle / (2 * Math.PI)) * items.length) % items.length;
                                    const selectedItem = items[selectedIndex];
                                    setTimeout(() => {{
                                        alert("🍽 오늘의 추천 메뉴는: " + selectedItem);
                                    }}, 100);
                                    isSpinning = false;
                                }}
                                ctx.clearRect(0, 0, size, size);
                                ctx.save();
                                ctx.translate(centerX, centerY);
                                ctx.rotate(angle);
                                ctx.translate(-centerX, -centerY);
                                drawWheel();
                                ctx.restore();
                            }}, 16);
                        }}

                        drawWheel();
                        document.getElementById("spinButton").addEventListener("click", spinWheel);
                    </script>
                </body>
                </html>
            ' width="430" height="500" style="border:none;"></iframe>
        </div>
        """,
        unsafe_allow_html=True
    )
