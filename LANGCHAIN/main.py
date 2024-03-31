# to run the file just write -> streamlit run main.py

# Integrate our code with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
# For UI purposes
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# streamlit framework
st.title("LangChain Demo with OPENAI API")
input_text = st.text_input("Search the topic you want")

# openai llms
llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
