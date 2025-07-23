import streamlit as st
import time
import random

# 초기 상태
if 'running' not in st.session_state:
    st.session_state.running = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'elapsed' not in st.session_state:
    st.session_state.elapsed = 0
if 'quote' not in st.session_state:
    st.session_state.quote = "🧠 시작하면 명언이 나옵니다!"

quotes = [
    "작은 성취도 반복되면 큰 성공이 된다.",
    "오늘 걷지 않으면 내일은 뛰어야 한다.",
    "포기하지 마라. 끝까지 해보자.",
    "지금 흘리는 땀이 내일의 성적을 만든다.",
    "노력은 배신하지 않는다.",
    "지금 이 순간이 가장 중요하다.",
    "계획 없는 목표는 단지 소원일 뿐이다."
]

def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02}:{secs:02}"

st.title("⏱ 공부 타이머 + 명언 생성기")
st.info(st.session_state.quote)

TIMER_SECONDS = 25 * 60

if st.session_state.running:
    st.session_state.elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(TIMER_SECONDS - st.session_state.elapsed, 0)
else:
    remaining = max(TIMER_SECONDS - st.session_state.elapsed, 0)

st.header(f"⏳ 남은 시간: {format_time(remaining)}")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶️ 시작"):
        if not st.session_state.running:
            st.session_state.running = True
            st.session_state.start_time = time.time() - st.session_state.elapsed
            st.session_state.quote = "💬 " + random.choice(quotes)
            st.experimental_rerun()

with col2:
    if st.button("⏸ 일시정지"):
        if st.session_state.running:
            st.session_state.running = False
            st.session_state.elapsed = int(time.time() - st.session_state.start_time)
            st.experimental_rerun()

with col3:
    if st.button("🔄 리셋"):
        st.session_state.running = False
        st.session_state.start_time = None
        st.session_state.elapsed = 0
        st.session_state.quote = "🧠 시작하면 명언이 나옵니다!"
        st.experimental_rerun()

if remaining == 0 and st.session_state.running:
    st.success("🎉 25분 집중 완료! 잠깐 쉬어가요.")
    st.session_state.running = False
