from openai import OpenAI
import os

#os.environ["OPENAI_API_KEY"] = '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'

#os.environ["OPENAI_API_KEY"] = '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'

#os.environ["OPENAI_API_KEY"] = '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'

os.environ["OPENAI_API_KEY"] = 'IdmjrNpfm100'

client = OpenAI()
OpenAI.api_key = os.getenv('OPENAI_API_KEY')


def generate_data(query):
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[  # Change the prompt parameter to messages parameter
            {'role': 'user', 'content': query}],
        temperature=0
    )
    data = completion.choices[0].message.content
    return data
