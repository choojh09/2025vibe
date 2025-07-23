import streamlit as st
import random

# 초기 잔액 설정
if 'balance' not in st.session_state:
    st.session_state.balance = 1000

# 앱 제목
st.title("🐉🐯 용 vs 호 가상 베팅 게임")
st.subheader("가상 코인을 걸고 승부를 예측하세요!")

# 현재 잔액 표시
st.markdown(f"### 💰 현재 잔액: `{st.session_state.balance}` 코인")

# 베팅 금액 입력
bet_amount = st.number_input("베팅 금액", min_value=10, max_value=st.session_state.balance, value=100, step=10)

# 선택 버튼 (용 or 호)
col1, col2 = st.columns(2)

with col1:
    dragon_bet = st.button("🐉 용에 베팅")

with col2:
    tiger_bet = st.button("🐯 호에 베팅")

# 결과 처리 함수
def play_game(player_choice):
    result = random.choice(["용", "호"])
    win = (player_choice == result)

    if win:
        st.success(f"🎉 결과: {result}! 승리! {bet_amount}코인 획득!")
        st.session_state.balance += bet_amount
    else:
        st.error(f"😢 결과: {result}! 패배... {bet_amount}코인 잃음.")
        st.session_state.balance -= bet_amount

    st.markdown(f"### 💼 남은 잔액: `{st.session_state.balance}` 코인")

# 베팅 시 실행
if dragon_bet:
    play_game("용")

elif tiger_bet:
    play_game("호")

# 잔액 부족 시
if st.session_state.balance <= 0:
    st.warning("잔액이 0입니다. 다시 시작하려면 페이지를 새로고침하세요.")

# 하단 설명
st.markdown("---")
st.caption("※ 실제 돈이 아닌 가상 코인으로만 플레이되는 시뮬레이션 게임입니다.")
