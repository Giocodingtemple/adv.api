import requests
import json 
import base64
from getpass import getpass
import time
from datetime import *
import random

url = 'https://cae-bootstore.herokuapp.com/question'

endpoint_login = "/login"
endpoint_user = "/user"
endpoint = "/question"



def post_question(token, payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json',
        'Authorization':'Bearer ' + token
    }
    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text


Gios_payload={
       {
            "answer": "Towel",
            "question": "What gets wetter as it dries?"
        },
       {
            "answer": "Pennywise",
            "question": "What is bright red and white all over?"
        },
	   {
            "answer": "Mercury",
            "question": "Hg is the chemical symbol of which element?"
        },
       {
            "answer": "Hotmail",
            "question": "Which email service is owned by Microsoft?"
        },
       {
            "answer": "Brazil",
            "question": "Which country produces the most coffee in the world?"
        },
       {
            "answer": "Paris",
            "question": "In which city was Jim Morrison buried?"
        },
       {
            "answer": "Delaware",
            "question": "What was the first state?"
        },
	   {
            "answer": "Madrid",
            "question": "What is the capital city of Spain?"
        },
       {
            "answer": "The Mona Lisa",
            "question": "What is the painting “La Gioconda” more usually known as?"
        },
       {
            "answer": "10,000",
            "question": "About how many taste buds does the average human tongue have?"
        }

}

#post_questions(gm['token'], gios_payload)
post_question(Gios_payload) 

def register_user(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json'
    }
    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text

def login_user(user_name, password):
    auth_string = user_name + ":" + password
    
    headers={
        'Authorization' : "Basic "+base64.b64encode(auth_string.encode()).decode()
    }
    
    user_data = requests.get(
        url + endpoint_login,
        headers=headers
    )
    return user_data.json()

login_user('gmarchiori5149@gmail.com', '123')
gm = login_user('gmarchiori5149@gmail.com', '123')


def delete_question(token):
    headers = {
        'Authorization':"Bearer " + token
    }
    
    response = requests.delete(
        url+endpoint_user,
        headers=headers
    )
    return response.text

def edit_user(token, payload):
    payload_json_string=json.dumps(payload)
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Bearer ' + token
    }

    response=requests.put(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.status_code

def login(email):
    clear_output()
    password=getpass("Password: ")
    user = login_user(email, password) 
    return user

def register():
    clear_output()
    print("Registration:")
    email = input("Email: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    password = getpass("Password: ")
    
    user_dict={
        "email":email,
        "first_name":first_name,
        "last_name":last_name,
        "password":password
    }
    return register_user(user_dict)

def do_login_user():
    #name = login_user(email, password)
 
    while True:
        clear_output()
        print("Welcome to the Bookstore")
        email = input("Type your email to login or Type `register` to Register ")
        if email == 'register':
            success_register=register()
            if success_register:
                print("You have successfully registered")
                continue
        elif email.lower() == "quit":
            print("Goodbye")
            break
        else:
            try:
                return login(email)                 
            except:
                print("Invalid Username/Password combo")
                time.sleep(2)
                continue
                
def questions():
    questions = [
        {
            "answer": "Towel",
            "question": "What gets wetter as it dries?"
        },
        {
            "answer": "Pennywise",
            "question": "What is bright red and white all over?"
        },
	  {
            "answer": "Mercury",
            "question": "Hg is the chemical symbol of which element?"
        },
        {
            "answer": "Hotmail",
            "question": "Which email service is owned by Microsoft?"
        },
        {
            "answer": "Brazil",
            "question": "Which country produces the most coffee in the world?"
        },
        {
            "answer": "Paris",
            "question": "In which city was Jim Morrison buried?"
        },
        {
            "answer": "Delaware",
            "question": "What was the first state?"
        },
	  {
            "answer": "Madrid",
            "question": "What is the capital city of Spain?"
        },
        {
            "answer": "The Mona Lisa",
            "question": "What is the painting “La Gioconda” more usually known as?"
        },
        {
            "answer": "10,000",
            "question": "About how many taste buds does the average human tongue have?"
        }
    ]
    