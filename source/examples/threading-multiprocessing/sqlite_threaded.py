import logging
import os
import sys
import sqlite3
import threading
import time
import random
import string


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-10s) %(message)s',
                    )

DB_FILENAME = 'test.db'

def populate_db():
    with sqlite3.connect(DB_FILENAME) as conn:
        conn.execute("""CREATE TABLE BOOKS(author VARCHAR, title VARCHAR)""")

def show_books(conn):
    for i in range(100):
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM BOOKS LIMIT 1""")
        for row in cursor:
            print(row)
    
def writer():
    with sqlite3.connect(DB_FILENAME) as conn:
        for i in range(100):
            cursor = conn.cursor()
            first_letter = random.choice(string.ascii_uppercase)
            author = first_letter + ''.join(random.choices(string.ascii_lowercase, k=random.choice(range(5,9))))
            first_letter = random.choice(string.ascii_uppercase)
            book = first_letter + ''.join(random.choices(string.ascii_lowercase, k=random.choice(range(4,12))))
            data = [author, book]
            #print('data', data)
            cursor.execute("INSERT INTO BOOKS(author, title) VALUES (?, ?)", data)
            conn.commit()

def reader():
    with sqlite3.connect(DB_FILENAME) as conn:
        show_books(conn)

if __name__ == '__main__':

    if os.path.exists(DB_FILENAME):
        os.remove(DB_FILENAME)
    
    populate_db()
    ready = threading.Event()
        
    threads = [
        threading.Thread(name="Reader", target=reader, args=()),
        threading.Thread(name="Writer", target=writer, args=()),
        ]
        
    [t.start() for t in threads]
        
    [t.join() for t in threads]
