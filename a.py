import streamlit as st
print('test')
st.write('Hello')
st.title('Assignment 1')
name = st.text_input('Your name:')
if st.button('Submit'):
    st.write('Hello,' + name)