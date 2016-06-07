import sqlite3
import sys


def dict_to_db(dict_of_words):
    try:
        bd_name = sys.argv[2]
    except IndexError:
        bd_name = 'myWordsDB.sqlite'

    conn = sqlite3.connect(bd_name)
    cur = conn.cursor()
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS Words (
        id      INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
        word    TEXT UNIQUE NOT NULL,
        count   INTEGER NOT NULL
    )
    ''')
    for key, value in dict_of_words.items():
        try:
            cur.execute('''INSERT INTO Words (word, count) VALUES ( ?, ? )''',
                        (key, value, ))
            conn.commit()
        except sqlite3.IntegrityError:
            continue
