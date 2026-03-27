from bottle import post, request
import re
from datetime import datetime
import pdb

questions = {}

@post('/home', method='post')
def my_form():

    question = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')
    email = request.forms.get('ADRESS')
    

    if not question or not username or not email or question.strip() == "" or username.strip() == "":
        return "Error! All fields must be filled!"
  

    email_pattern = r'^[a-zA-Z0-9]{4,19}@[a-zA-Z0-9.-]{2,10}\.[a-zA-Z]{2,5}$'
    if not re.match(email_pattern, email):
        return "Error! Invalid email format!"
    
    questions[email] = [username, question]
    pdb.set_trace()

    current_date = datetime.now().strftime("%d-%m-%Y")
    
    return f"Thanks, {username}! The answer will be sent to {email}. Access Date: {current_date}"

