# database.py
import sqlite3
from datetime import datetime
import pyrebase

firebaseConfig={
    'apiKey': "AIzaSyBUTX8Rim1OMPAKOMFjRzsf4CHmPW_6gMY",
    'authDomain': "authdemo-79174.firebaseapp.com",
    'databaseURL':"https://authdemo-79174.firebase.com",
    'projectId': "authdemo-79174",
    'storageBucket': "authdemo-79174.appspot.com",
    'messagingSenderId': "498091607020",
    'appId': "1:498091607020:web:0142211b6f901ad33cf6c9",
    'measurementId': "G-R733GSGM2L"}

firebase=pyrebase.initialize_app(firebaseConfig)

auth=firebase.auth()

class Database:
    def __init__(self):
        #self.conn = sqlite3.connect('database.db')
        #self.create_tables()
        self.conn = sqlite3.connect("database.db")
        self.create_tables()

    def create_tables(self):
        try:
            with self.conn:
                cursor = self.conn.cursor()
                print("Creating tables")

                # User table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        worker_name TEXT NOT NULL,
                        worker_id TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )
                ''')
                print("passed user table")

                # Log table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        worker_name TEXT NOT NULL,
                        worker_id TEXT NOT NULL,
                        timestamp TEXT NOT NULL,
                        images TEXT NOT NULL,
                        num_rice_packages INTEGER NOT NULL,
                        arborio_percentage INTEGER NOT NULL,
                        basmati_percentage INTEGER NOT NULL,
                        ipsala_percentage INTEGER NOT NULL,
                        jasmine_percentage INTEGER NOT NULL,
                        karacadag_percentage INTEGER NOT NULL,
                        final_rice_type TEXT NOT NULL
                    )
                ''')

            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")


    def authenticate_user(self, worker_id, password):
        cursor = self.conn.cursor()
        query = 'SELECT password FROM users WHERE worker_id=?'
        cursor.execute(query, (worker_id,))
        #query = 'SELECT password FROM users WHERE worker_id =\'' + worker_id + "\'"
        #cursor.execute(query)
        #cursor.execute('SELECT * FROM users WHERE worker_id=? AND password=?', (worker_id, password))
        return cursor.fetchone() is not None

    def add_user(self, email, password):
        print("add user")
        auth.create_user_with_email_and_password(email, password)
        print("Add uswer")
        #login = Login()
        #widget.addWidget(login)
        #widget.setCurrentIndex(widget.currentIndex() + 1)


    def save_log(self, worker_name, worker_id, images, num_rice_packages, percentages, final_rice_type):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO logs (
                worker_name, worker_id, timestamp, images, num_rice_packages,
                arborio_percentage, basmati_percentage, ipsala_percentage,
                jasmine_percentage, karacadag_percentage, final_rice_type
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            worker_name, worker_id, timestamp, ','.join(images), num_rice_packages,
            percentages['arborio'], percentages['basmati'], percentages['ipsala'],
            percentages['jasmine'], percentages['karacadag'], final_rice_type
        ))

        self.conn.commit()


#db = Database()
#db.create_tables()
