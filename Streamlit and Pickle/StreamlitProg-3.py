import streamlit as st

# title
st.title("More GUI components...")
# button
if (st.button("Click Me")):
    st.write("Button has been CLICKED !!!")
else:
    st.write("Button has NOT been CLICKED !!!")
# checkbox
checkbox_state = st.checkbox("Check me to enable something...")
if checkbox_state:
    st.write("Checkbox is CHECKED !!!")
else:
    st.write("Checkbox is NOT CHECKED !!!")
# radio button
radio_selection = st.radio("Choose and Option:",
 ["Math","Pandas","Numpy","ScikitLearn","Seaborn","MatPlotLib"])
st.write("You selected:", radio_selection)
# selectbox
selectbox_selection=st.selectbox("Choose an item:",
        ["List","Tuple","Dictionary","Set","Frozen Set"])
st.write("You selected:", selectbox_selection)
# multiselect
multiselect_selection=st.multiselect("Choose multiple items:",
["Case sensative","OOP","Zero base","Functional","Iterative"])
st.write("You selected:", multiselect_selection)
# select slider
select_slider1 = st.select_slider("Select a value:",
                                  options=range(10))
st.write("Selected slider value:", select_slider1)
select_slider2 = st.select_slider("Select a value:",
                options=[1,4,5,6,3,2,"NLP"])
st.write("Select slider value:", select_slider2)





