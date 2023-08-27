import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('mnistやってみた')

st.button("Start", type="primary")
if st.button("Reset"):
    st.write("結果をResetしました")
else:
    st.write("Goodbye")
    
latest_iteration = st.empty()
bar = st.progress(0)

st.write("Starting")
for i in range(100):
    latest_iteration.text(f'Now Loading {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
st.write("done!!")