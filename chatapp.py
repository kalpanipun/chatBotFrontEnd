import streamlit as st
import warnings
import os
import re
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Reading Methods
from functions import generate_data
from read_data import load_index
from read_data import load_pdf

# Data path
file_path = 'financial_statements_csv.csv'

stock_path = 'stock_mkt_data4.csv'

# hide future warnings (caused by st_aggrid)
warnings.simplefilter(action='ignore', category=FutureWarning)

# set page layout and define basic variables
st.set_page_config(layout="wide", page_icon='⚡', page_title="Instant Insight")
path = os.path.dirname(__file__)
# today = date.today()

# create sidebar filters
############################ All the markdowns #############################################

################## Logo ###################################################
st.markdown(
    """
    <style>
    .logo-container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    .logo-img {
        max-width: 100px; /* Adjust the max-width as needed */
        height: auto;
    }
    </style>
    """
    , unsafe_allow_html=True
)
# Logo container
st.markdown('<div class="logo-container">', unsafe_allow_html=True)
# Logo image
st.markdown('<img src="https://i.ibb.co/Dz3rmgq/logo-copy.png" class="logo-img">', unsafe_allow_html=True)
# Close the logo container
st.markdown('</div>', unsafe_allow_html=True)
#########################################################################################


##################### button,Text and background colour ########################################
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #007bff; /* Blue color for buttons */
        color: #ffffff; /* White text color for buttons */
    }
    .stTextInput>div>div>input {
        background-color: #ffffff; /* White color for text input boxes */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# background colour

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #FFD700, #FFA500); /* Gradient background colors */
        font-family: Arial, sans-serif; /* Set font family */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Text Box
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        border: 1px solid #0e2f44; /* Add a 1px solid border with gray color */
        padding: 8px; /* Add padding to the input elements */
        border-radius: 4px; /* Add border radius for rounded corners */
    }
    </style>
    """,
    unsafe_allow_html=True
)
###############################################################################

st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #00FF00 !important; /* Green color */
    }
    </style>
    <div style="position: fixed; bottom: 10px; left: 10px;">
        <p style="font-size: 12px;"> Developed by OCTBOTS team </p>
    </div>
    """,
    unsafe_allow_html=True
)

#############################################################################################

st.sidebar.write('**How to use this application??** ')
st.sidebar.write('1. Provide your investment objective and risk appetite to get the best fitting stocks for your portfolio!?? ')
st.sidebar.write('2. Visualize the stocks in any fashion to make an informed decision.')

with st.expander('Future of this app'):
    st.write('''
    To update it to match the CSE 
    ''')

##############################################################################################################

index = load_index(stock_path)
chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(), chain_type="stuff",
                                    retriever=index.vectorstore.as_retriever(), input_key="question")

st.title('Your Financial Advisor! 💰')

user_query = st.text_input('Ask anything about the stocks : ', '')
template = (f"{user_query},If there are any graphs to be plot give python code for that")



# Create a placeholder for the response
response_placeholder = st.empty()
send_button = st.button('Send')

# Create a button to submit the query and trigger the conversation flow
if send_button:
    # Generate a response based on the user's query


    index = load_index(stock_path)

    # chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(), chain_type="stuff",
    #                                     retriever=index.vectorstore.as_retriever(), input_key="question")

    # response = chain({"question": template})

    result = index.query(template, llm=ChatOpenAI())

    # Remove python code from the output

    # pattern = r"(?s)(?<!```python\n)(.*?)(?!```)"
    # extracted_text = re.findall(pattern, response['result'])
    # st.write(extracted_text)

    code_match = re.search(r'```python\n(.*?)\n```', result, re.DOTALL)
    if code_match:
        generated_code = code_match.group(1)

        try:
            exec(generated_code)

            st.pyplot()

        except Exception as e:
            st.error(f"Error executing code: {e}")

# personal data

personal_query = st.text_input('Tell us about your personal financial goal to generate the best stocks that fit you: ', '')
response_placeholder_p = st.empty()
send_button_p = st.button('Go')

static_query_template_p = (f"I have given a historical dataset on stock market prices for 7 assets. Act as a helpful "
                           f"financial advisor."
                           f"Map the appropriate stocks based on my personal specifications. "
                           f"In order to map, take into account the stock return, "
                           f"coefficient of variation to make a decision. {personal_query} "
                           f"Which stocks are appropriate for me?" 
                           f"Provide a short answer,If there are any graphs to be plot give python code for that")

if send_button_p:

    result_p = index.query(static_query_template_p, llm=ChatOpenAI())
    st.write(result_p)

    code_match = re.search(r'```python\n(.*?)\n```', result_p, re.DOTALL)
    if code_match:
        generated_code = code_match.group(1)

        try:
            exec(generated_code)

            st.pyplot()

        except Exception as e:
            st.error(f"Error executing code: {e}")



