#author = Tahmid Bin Taslim Rafi
#Date: 24/08/2021
#Path: adaptivityai.py
#Description: This is a simple chatbot that uses the openai library to generate a response to a given question.
#importing all the required libraries
import os
from random import choice

import openai
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()
openai.api_key = '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'
completion = openai.Completion()

start_sequence = "\nAva:"
restart_sequence = "\n\nHuman:"
session_prompt= """Ava: Hi!! It's a pleasure getting to talk to you. My name is  Ava, a friendly AI and Adaptivity's evangelist. I'm an expert in digital skills, digital careers, and most importantly, digital employability. If you are thinking about making a shift in the digital economy, I would be happy to help you :)\n\nHuman: so, which digital career is right for me?\nAva: Many factors come into play. This could vary from compensation, workload, freedom, industry, colleagues, work environment, and so on. From my experiences, you should go for the career that fits naturally with your [Digital Skills Archetype] (https://www.adaptivity.us/skillsarchetypes/). """
def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt_text,
      temperature=0.9,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
      stop=["\n", " Human:", " Ava:"]
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
