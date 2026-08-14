import streamlit as st

# title
st.title("Streamlit text input Examples...")
# text input
name=st.text_input("Enter your name: ")
# text area
feedback=st.text_area("Enter your feedback: ")
# number input
age=st.number_input("Enter your age: ",min_value=0,
                    max_value=100,step=1)
# date input
date=st.date_input("Select a date: ")
# time input
time=st.time_input("Select a time: ")
# color picker
color=st.color_picker("Select a color: ")
# accepting all the inputs
st.write("Name:", name)
st.write("Feedback:", feedback)
st.write("Age:", age, "years")
st.write("Date:", date)
st.write("Time:", time)
st.write("Color:", color)







