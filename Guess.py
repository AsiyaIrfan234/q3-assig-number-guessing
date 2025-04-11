import streamlit as st
import random

st.title("🎯 Number Guessing Game")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

guess = st.number_input("Guess the number (1-100):", min_value=1, max_value=100, step=1)
submit = st.button("Submit Guess")

if submit:
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.warning("📉 Too Low!")
    elif guess > st.session_state.number:
        st.warning("📈 Too High!")
    else:
        st.success(f"🎉 Congratulations! You guessed it right in {st.session_state.attempts} attempts.")
        st.balloons()

        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0


if st.button("🔁 Reset Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.success("Game reset! Try again 🚀")

