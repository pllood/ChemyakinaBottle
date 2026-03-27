from bottle import post, request
import re
from datetime import datetime
import pdb
import json
import os

fileData = 'questions.json'

@post('/home', method='post')
def my_form():

    question = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')
    email = request.forms.get('ADRESS')
    

    if not question or not username or not email or question.strip() == "" or username.strip() == "":
        return "Error! All fields must be filled!"
  
    if len(question) <= 3:
        return "Error! Question must be longer than 3 characters!"

    if question.isdigit():
        return "Error! Question cant be just numbers"

    email_pattern = r'^[a-zA-Z0-9]{4,19}@[a-zA-Z0-9.-]{2,10}\.[a-zA-Z]{2,5}$'
    if not re.match(email_pattern, email):
        return "Error! Invalid email format!"

    if os.path.exists(fileData):
        with open(fileDate) as json_file:
            data = json.load(json_file)
    else:
        data = {}

    if email not in data:
        data[email] = []

    if question not in data[email]:
        data[email].append(question)

   
    pdb.set_trace()

    with open(fileDate, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    current_date = datetime.now().strftime("%d-%m-%Y")
    
    return f"Thanks, {username}! The answer will be sent to {email}. Access Date: {current_date}"

