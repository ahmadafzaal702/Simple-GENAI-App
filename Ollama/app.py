from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import os
from dotenv import load_dotenv

## load the environment variables
load_dotenv()

## llm configuration and output parser
llm = ChatOllama(model="llama3.2:1b")
output_parser = StrOutputParser()

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant. Please respond to the question asked'),
        ('user','Question: {question}'),
    ]
)

## chain
chain = prompt|llm|output_parser

## streamlit web app

st.title("Simple Chatbot application")
input_text = st.text_input("What question you have in mind?")

if input_text:
    result = chain.invoke({'question':{input_text}})
    st.write(result)
