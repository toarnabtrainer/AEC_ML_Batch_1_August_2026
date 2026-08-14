# pip install streamlit
# streamlit --help
# pip uninstall streamlit
# streamlit run pythonscript.py

import streamlit as st

# title
st.title("Machine Learning Project...")
# header / subheader
st.header("This is a header.")
st.subheader("This is a sub-header.")
# text
st.text("Hello Streamlit !!!")
# markdown
st.markdown("# Heading - 1")
st.markdown("## Heading - 2")
st.markdown("### Heading - 3")
st.markdown("#### Heading - 4")
st.markdown("##### Heading - 5")
st.markdown("###### Heading - 6")
# error and colorful text
st.success("Successful message...")
st.info("Information message...")
st.warning("Warning message...")
st.error("Error message...")
# exception
st.exception("NameError('Name pd not defined')")
import math
st.help(math.pow)
st.help(print)
# writing text super function
st.write("Text with write...")
st.write(range(10))
st.write(list(range(10)))
# working with the media file
from PIL import Image
# PIL -> Python Imaging Library
img = Image.open("plot1.png")
st.image(img)
st.image(img, width = 300, caption = "Sinusoidal Waveform")
st.image("plot1.png")
st.video("rain.mp4")
st.audio("Tune1.aac")





