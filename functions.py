from langchain_openai import ChatOpenAI
import streamlit as st
from openai import OpenAI
import matplotlib.pyplot as plt
import os
import re

os.environ["OPENAI_API_KEY"] = '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'

client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')

def generate_data(query):

    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[  # Change the prompt parameter to messages parameter
            {'role': 'user', 'content': query} ],
        temperature=0
    )

    data = completion.choices[0].message.content
    return data


def extract_data(api_output):
    # Regular expression pattern to match the data lines
    pattern = r'(\d{4}): \$([\d,]+)'
    matches = re.findall(pattern, api_output)
    years = [int(match[0]) for match in matches]
    revenues = [int(match[1].replace(',', '')) for match in matches]
    return years, revenues

def create_bar_graph(data):
    years, revenues = extract_data(data)
    plt.bar(years, revenues)
    plt.xlabel('Year')
    plt.ylabel('Sales Revenue ($)')
    plt.title('Sales Revenue Over the Past 5 Years')
    st.pyplot()