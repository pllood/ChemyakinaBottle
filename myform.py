from bottle import post, request
import re
from datetime import datetime
import json
import os

fileData = 'question.json'

@post('/home', method='post')
def my_form():

    question = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')
    email = request.forms.get('ADRESS')
    
      # Проверка, чтобы все поля были заполнены
    if not question or not username or not email or question.strip() == "" or username.strip() == "":
        return "Error! All fields must be filled!"
  
    # Проверка, чтобы длина вопроса была больше 3 символов
    if len(question) <= 3:
        return "Error! Question must be longer than 3 characters!"

    # Проверка, чтобы длина имени пользователя была больше 2 символов
    if len(username) <= 2:
        return "Error! Username must be longer than 2 characters!"

    # Проверка, чтобы вопрос не состоял только из цифр
    if question.isdigit():
        return "Error! Question cant be just numbers"

    # Проверка, чтобы вопрос содержал хотя бы одну латинскую букву
    if not re.search(r'[a-zA-Z]', question):
        return "Error! Question must contain letters!"

    # Регулярное выражение для вопроса
    question_pattern = r'^[A-Za-z0-9\s\?\.,!;:-]+$' 

     # Проверка, чтобы вопрос состоял из разрешенных символов
    if not re.match(question_pattern, question):
        return "Error! Ivalid question format!"

    # Регулярное выражение для имени пользователя
    username_pattern = r'^[A-Za-z0-9]+$'

    # Проверка, чтобы имя состояло из разрешенных символов
    if not re.match(username_pattern, username):
        return "Error! Invalid username format!"

    # Регулярное выражение для почты
    email_pattern = r'^[a-zA-Z0-9]{4,19}@[a-zA-Z0-9.-]{2,10}\.[a-zA-Z]{2,5}$'

    # Проверка, чтобы почта состояла из разрешенных символов
    if not re.match(email_pattern, email):
        return "Error! Invalid email format!"

     # Проверка на существование файла
    if os.path.exists(fileData):
         # Если существует - открываем
        with open(fileData) as json_file:
             # Загружаем 
            data = json.load(json_file)
    else:
         # Если файла нет, то создаем пустой словарь
        data = {}

    # Если почты нет в файле, то создаем для нее пустой список
    if email not in data:
        data[email] = []

    # Приводим вопрос к нижнему регистру
    question_lower = question.lower()

    # Проверка, чтобы такого вопроса не было
    duplicate = False
    for existing_question in data[email]:
        if existing_question.lower() == question_lower:
            duplicate = True
            break
    
    if duplicate:
        return "Error! This question already exists!"

    # Если вопроса нет, то добавляем его
    data[email].append(question)

    # Сохранение файла
    with open(fileData, 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    current_date = datetime.now().strftime("%d-%m-%Y")
    
    return f"Thanks, {username}! The answer will be sent to {email}. Access Date: {current_date}"

