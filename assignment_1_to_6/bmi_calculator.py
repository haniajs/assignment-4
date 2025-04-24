import streamlit as st
import time

st.set_page_config(page_title="BMI Calculator", page_icon="🌡️", layout="centered")
st.title("BMI Calculator")
st.markdown("""Calculate your body mass index in bmi calculator. Enter your height and weight below!""")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg): " , min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("Height (m): " , min_value=1.0, format="%.2f")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.subheader("Your bmi is: ")
    st.markdown(f"{bmi:.2f}",unsafe_allow_html=True)

    if bmi < 18.5:
        st.error("underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("normal weight")
    elif 25 <= bmi < 29.9:
        st.warning("overweight")
    else:
        st.error("Obesity")
else:
    st.info("please enter a valid weight and height")
