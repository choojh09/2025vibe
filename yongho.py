import streamlit as st
import random

st.set_page_config(page_title="랜덤 심리 테스트", layout="centered")

st.title("🧠 랜덤 심리 테스트")
st.markdown("재미로 보는 성격 유형! 아래 질문에 답해보세요.")

# 질문 리스트
questions = [
    {
        "question": "친구가 약속 시간에 늦었을 때 당신은?",
        "options": {
            "괜찮아~ 기다릴 수 있어.": "고래",
            "조금 짜증나지만 참는다.": "고양이",
            "왜 늦었는지 바로 물어본다.": "호랑이",
            "나도 늦게 간다.": "여우"
        }
    },
    {
        "question": "주말에 가장 하고 싶은 활동은?",
        "options": {
            "집에서 푹 쉬기": "고양이",
            "산책이나 운동": "호랑이",
            "책 읽기, 공부": "고래",
            "친구들이랑 놀기": "여우"
        }
    },
    {
        "question": "시험이 내일인데 아직 공부 안 했다면?",
        "options": {
            "벼락치기 시작!": "호랑이",
            "포기하고 잠이나 잔다...": "고양이",
            "최대한 해보려고 노력한다.": "고래",
            "친구에게 답 물어본다": "여우"
        }
    }
]

animal_points = {"고래": 0, "고양이": 0, "호랑이": 0, "여우": 0}

# 선택지 진행
for q in questions:
    st.subheader(q["question"])
    choice = st.radio("선택하세요", list(q["options"].keys()), key=q["question"])
    selected_animal = q["options"][choice]
    animal_points[selected_animal] += 1

# 결과 보기 버튼
if st.button("🔮 결과 보기"):
    # 최다 득표 동물 찾기
    result = max(animal_points, key=animal_points.get)
    
    # 결과 출력
    st.markdown(f"## 당신은... 🐾 **{result}상** 입니다!")
    
    # 간단한 설명
    descriptions = {
        "고래": "조용하고 깊은 성찰형. 남을 잘 배려하는 타입!",
        "고양이": "귀찮음이 미덕인 자유로운 영혼!",
        "호랑이": "리더십 있고 추진력 강한 타입!",
        "여우": "눈치 빠르고 재치 있는 스타일!"
    }
    
    st.info(descriptions[result])

st.markdown("---")
st.caption("※ 재미로 즐겨주세요 😄 | 만든이: ChatGPT")
