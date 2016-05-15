import sqlite3


def dict_to_db(dict_of_words):
    # TODO Добавить проверку (Add Try-Exception)
    conn = sqlite3.connect('myWordsDB.sqlite')
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
