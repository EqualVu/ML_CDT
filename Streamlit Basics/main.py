import streamlit as st

st.title('My project in Streamlit')
st.header('This is a header')
st.subheader('This is a sub header')
st.divider()
st.markdown('#Heading 1')
st.markdown('My lesson for dummy  ')
st.markdown('[Van Lang University](https://elearning.vlu.edu.vn/?redirect=0)')
st.markdown("""
            1. Machine learning
            2. Deep learing
            """)
st.markdown(r'$\sqrt{2x} $')

st.divider()

st.latex(r'\sqrt{2x}')

st.divider()
st.write('[Google](https://discord.com/channels/586503387072167937/586588958885150721)')
st.write(r'$ \sqrt{2x} $')
st.write('1 + 1=',2)
st.divider()
st.image('D:\\Study stuff\\Machine Learning\\Git_Demo_CDT_01_K27\\ML_CDT\\gg.png','Funny picture')
st.audio('D:\\Study stuff\\Machine Learning\\Git_Demo_CDT_01_K27\\ML_CDT\\kh90.mp4')
st.divider()
st.video('D:\\Study stuff\\Machine Learning\\Git_Demo_CDT_01_K27\\ML_CDT\\kh90.mp4')
st.divider()

agree=st.checkbox("I agree!")
disagree=st.checkbox("I don't agree!")
if agree:
    st.write("Thanks!")
if disagree:
    st.write("Skill issue!")
status=st.radio('Your Favorite color: ',['Yellow','Blue'])
print(status)
options=st.multiselect('Colors:',['Green','Yellow','Blue'],['Yellow','Blue'])
print(options)

st.select_slider('Your color:',['Red','Yellow','Blue'])

st.divider()
name=st.text_input('Your name: ',value='Guest')
st.write(name)
if st.button('Submit'):
    st.write("Hello =")
else:
    st.write("Goodbye")
st.divider()
files=st.file_uploader('Please up load file: ',accept_multiple_files=True)
for file in files:
    read_f=file.read()
    st.write('File name: ',file.name)
st.divider()
#with st.form('Infomation of Exercises'):
 #   col1,col2=st.columns(2)
  #  f_name=col1.text_input('Name')
   # f_age=col2.text_input('Age')
    #sumbmits=st.form_submit_button('Save')
    #if sumbmits:
     #   st.write(f"Name: {f_name}, Age: {f_age}")
st.divider()