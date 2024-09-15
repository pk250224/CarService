import google.generativeai as ai
import os
from dotenv import load_dotenv
import promt as ut
import gradio as gr
import csv
import pandas as pd
# Configure api_key

#ai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

ai.configure(api_key='AIzaSyCv-aW0wS9pCujlXiKe1Ttxlpz0jn0TbpQ')
#Define Model Instance
model = ai.GenerativeModel('gemini-pro')
history=[
        {"role": "user", "parts": "Hello, I am Pardeep"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
chat = model.start_chat(history=[])

# print(chat)

# Function to get a response from the AI model based on the provided prompt

def get_response(prompt):
    response = chat.send_message(prompt)
    print(response.text)
    return response.text

# prompt="What is my name?"
# get_response(prompt)

df = pd.read_csv('src/CarData.csv',engine='python')

carData = f"""Car Data :  {df.to_string()}"""

# print(chat.history)

context =  ut.content()

context.append(carData)

print(context)

context.append("")
response = get_response(context)
print(response)

def chatbot(message, history):
  prompt = message
  context.append(prompt)
  response = get_response(context)
  context.append(response)
 # print(context)
  return response

gr.ChatInterface(fn=chatbot, examples=["Personal Loan", "Home Loan", "Car Loan"], title='Loan Automate Service').launch(debug=True, share=True)