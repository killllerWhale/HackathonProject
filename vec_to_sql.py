import pyrebase
import csv

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

auth = firebase.auth()
#
login = "ruslan@gmail.com"
password = "12345678"

# auth.create_user_with_email_and_password(login, password)

auth.sign_in_with_email_and_password(login, password)
db = firebase.database()


def parsi():
    with open("book.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            for elem in range(len(row)):
                if len(row[1].split()) > 13:
                    if elem == 0:
                        elem1 = row[elem]
                    elif elem == 1:
                        elem2 = row[elem]
            data = {f"{elem1}": f"{elem2}"}
            db.push(data)


parsi()
