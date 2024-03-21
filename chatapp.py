import streamlit as st
#from streamlit_dynamic_filters import DynamicFilters
# from st_aggrid import AgGrid
# from st_aggrid.grid_options_builder import GridOptionsBuilder
# from st_aggrid import GridUpdateMode, DataReturnMode
import warnings
# import plotly.express as px
# import plotly.graph_objects as go
# import requests
import os
# import ast
# from io import BytesIO
import openai

from functions import generate_data
from functions import create_bar_graph



# hide future warnings (caused by st_aggrid)
warnings.simplefilter(action='ignore', category=FutureWarning)

# set page layout and define basic variables
st.set_page_config(layout="wide", page_icon='⚡', page_title="Instant Insight")
path = os.path.dirname(__file__)
#today = date.today()

# create sidebar filters
st.sidebar.write('**Select the sector if you want** 👇')

with st.sidebar:
    options = ['Banking', 'Finance', 'Insurance']

    # Create a dropdown menu using st.selectbox
    selected_option = st.selectbox('Choose from available sectors', options)

    # Display the selected option
    st.write('You selected:', selected_option)
    st.markdown("Developed by OCTOBOTS team")
##############################################################################################################

st.title('Your Financial Advisor !')

with st.expander('What is this app about?'):
    st.write('''
    This app is designed to generate an instant company research.\n
    In a matter of few clicks, a user gets details about ...

    Use Case Example:\n
    

    Tech Stack:\n
    
    ''')

user_query = st.text_input('Enter your query here:', '')

# Create a placeholder for the response
response_placeholder = st.empty()

send_button = st.button('Send')

def generate_response(query):
    return query

# Create a button to submit the query and trigger the conversation flow
if send_button:
    # Generate a response based on the user's query

    data = generate_data(user_query)
    st.write(data)

    #response = generate_response(user_query)
    # Display the response
    create_bar_graph(data)

    #response_placeholder.text_area('ChatGPT:', value=response, height=200)

    #user_query = st.text_input('You:', '')


# Display the user's query
#st.write('You entered:', user_query)


