import streamlit as st
import os
import json

OUTPUT_DIR="outputs"

st.title("Clara Agent Dashboard")

accounts=os.listdir(OUTPUT_DIR)

account=st.selectbox("Account",accounts)

memo=json.load(open(f"{OUTPUT_DIR}/{account}/memo.json"))

agent=json.load(open(f"{OUTPUT_DIR}/{account}/agent.json"))

st.subheader("Memo")
st.json(memo)

st.subheader("Agent")
st.json(agent)