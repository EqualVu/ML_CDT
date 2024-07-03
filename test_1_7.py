import streamlit as st

# Custom CSS to center the title
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 2.5em;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with the custom CSS class
st.markdown("<div class='centered-title'>streamlit hello</div>", unsafe_allow_html=True)
