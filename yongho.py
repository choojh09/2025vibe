import streamlit as st
import random
import time

# 카드 정의
card_values = {
    1: "A", 2: "2", 3: "3", 4: "4", 5: "5",
    6: "6", 7: "7", 8: "8", 9: "9", 10: "10",
    11: "J", 12: "Q", 13: "K"
}

# 상태 초기화
if 'balance' not in st.session_state:
    st.session_state.balance = 1000
if 'win_streak' not in st.session_state:
    st.session_state.win_streak = 0
if 'last_win' not in st.session_state:
    st.session_state.last_win = False

# 제목
st.set_page_config(page_title="용호 베팅 게임", layout="centered")
st.title("🐉🐯 용호(Dragon Tiger) 카드 베팅 게임")
st.markdown(f"### 💰 잔액: `{st.session_state.balance}` 코인")
st.markdown(f"🔥 현재 연승: `{st.session_state.win_streak}` 회")

# 베팅 UI
bet_amount = st.number_input("베팅 금액", min_value=10, max_value=st.session_state.balance, value=100, step=10)
bet_choice = st.radio("베팅 대상 선택:", ["용(Dragon)", "호(Tiger)", "무승부(Draw)"])

if st.button("🎴 카드 뽑기"):
    # 카드 무작위 추출
    dragon_card = random.randint(1, 13)
    tiger_card = random.randint(1, 13)

    # 애니메이션 느낌
    st.subheader("카드 공개 중...")
    with st.spinner("딜러가 카드를 준비하고 있습니다..."):
        time.sleep(1)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🐉 용(Dragon)**")
        st.markdown("<h1 style='text-align:center'>🂠</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown("**🐯 호(Tiger)**")
        st.markdown("<h1 style='text-align:center'>🂠</h1>", unsafe_allow_html=True)
    time.sleep(1)

    # 결과 표시
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<h1 style='text-align:center'>{card_values[dragon_card]}</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<h1 style='text-align:center'>{card_values[tiger_card]}</h1>", unsafe_allow_html=True)

    # 승부 판정
    if dragon_card > tiger_card:
        result = "용(Dragon)"
    elif tiger_card > dragon_card:
        result = "호(Tiger)"
    else:
        result = "무승부(Draw)"

    st.markdown(f"### 🎯 결과: **{result}**")

    # 결과 반영
    if bet_choice == result:
        if result == "무승부(Draw)":
            gain = bet_amount * 8
            st.success(f"🎉 무승부 적중! +{gain} 코인")
        else:
            gain = bet_amount
            st.success(f"✅ 적중! +{gain} 코인")
        st.session_state.balance += gain
        st.session_state.last_win = True
        st.session_state.win_streak += 1
    else:
        st.session_state.balance -= bet_amount
        st.error(f"❌ 틀렸습니다. -{bet_amount} 코인")
        st.session_state.last_win = False
        st.session_state.win_streak = 0

    st.markdown(f"💼 현재 잔액: `{st.session_state.balance}` 코인")
    st.markdown(f"🔥 현재 연승 기록: `{st.session_state.win_streak}` 회")

# 게임오버
if st.session_state.balance <= 0:
    st.warning("잔액이 0입니다. 새로고침하여 다시 시작하세요.")

st.markdown("---")
st.caption("※ 가상 코인 전용 게임입니다. 실제 도박이 아닙니다.")
