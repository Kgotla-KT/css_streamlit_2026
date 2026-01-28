# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("CSS 2026")

st.title("Title heading")

st.write("Hello, Streamlit_KG1!")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")

if st.button("Celebrate your first app!"):
    st.balloons()
    st.success("Congratulations, you are a Streamlit developer!")

st.markdown("I like Electrochemistry")