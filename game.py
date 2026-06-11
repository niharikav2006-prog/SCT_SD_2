import streamlit as st
import random

st.title("🎯 Guess the Number Game")

# Generate random number only once
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

st.write("I'm thinking of a number between **1 and 100**.")

guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=100,
    step=1
)

if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.secret_number:
        st.warning("📉 Too low! Try again.")
    elif guess > st.session_state.secret_number:
        st.warning("📈 Too high! Try again.")
    else:
        st.success(
            f"🎉 Congratulations! You guessed the number "
            f"{st.session_state.secret_number} in "
            f"{st.session_state.attempts} attempts."
        )

if st.button("New Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.rerun()