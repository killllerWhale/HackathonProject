import pyrebase
import json

config = {
    "apiKey": "AIzaSyBNnLM1ItodpQFU8jvkwuYOniyQ97VZADA",
    "authDomain": "bookfinder-97299.firebaseapp.com",
    "databaseURL": "https://bookfinder-97299-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "bookfinder-97299",
    "storageBucket": "bookfinder-97299.appspot.com",
    "messagingSenderId": "1079515581653",
    "appId": "1:1079515581653:web:57e569b2c6e82161e9265c",
    "measurementId": "G-V8NT67P272"
}

firebase = pyrebase.initialize_app(config)

login = "ruslan@gmail.com"
password = "12345678"

auth = firebase.auth()
auth.sign_in_with_email_and_password(login, password)

db = firebase.database()
