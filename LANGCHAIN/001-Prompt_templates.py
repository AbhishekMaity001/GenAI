# to run the file just write -> streamlit run main.py
# Integrate our code with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain import LLMChain  # this is responsible for executing the prompt template
from langchain.chains import SimpleSequentialChain, SequentialChain

from langchain.memory import ConversationBufferMemory

# For UI purposes
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# streamlit framework
st.title("LangChain Demo with OPENAI API")
input_text = st.text_input("Search the topic you want")

# Prompt templates
first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about {name} ?",
)
# Memory
person_memory = ConversationBufferMemory(input_key='name', memory_key='person_chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='dob_chat_history')
event_memory = ConversationBufferMemory(input_key='dob', memory_key='event_chat_history')


# openai llms
llm = OpenAI(temperature=0.8)
chain1 = LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='person', memory=person_memory)


second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="When was {person} born ?",
)
chain2 = LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='dob', memory=dob_memory)

# parent_chain = SimpleSequentialChain(chains=[chain1, chain2], verbose=True)

third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="Mention 5 major events happened around {dob} in the world ?",
)
chain3 = LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='event', memory=event_memory)

parent_chain = SequentialChain(
    chains=[chain1, chain2, chain3],
    input_variables=['name'],
    output_variables=['person', 'dob', 'event'],
    verbose=True
)

if input_text:
    st.write(parent_chain({'name': input_text}))

    with st.expander('Person Name'):
        st.info(dob_memory.buffer)

    with st.expander('Major Events'):
        st.info(event_memory.buffer)
