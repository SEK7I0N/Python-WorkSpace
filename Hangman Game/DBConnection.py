import sqlite3
import os
# Create/Connect to DB
#connection =sqlite3.connect("Dictionary.db")


connection =sqlite3.connect(':memory:')
cursor = connection.cursor()

#Create Table(s)
tbl_create_word = """CREATE TABLE IF NOT EXISTS TBL_WORD(
  WORD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  WORD VARCHAR(100) UNIQUE,
  WORD_LENGTH SMALLINT
);
"""
cursor.execute(tbl_create_word)

current_Path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def load_words():
    with open(os.path.join(current_Path, 'words_alpha.txt')) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def fetch_random_word(word_length):
    cursor.execute(("SELECT * FROM TBL_WORD where word_length = :word_len order by random() limit 1"),{'word_len': word_length})
    word = cursor.fetchone()
    return str(word)


def insert_word():
    english_words = load_words()

    for word in english_words:
        #Insert words into DB with length
        words={'word':word, 'word_len':len(word)}
        cursor.execute("INSERT INTO TBL_WORD(WORD, WORD_LENGTH) VALUES(:word, :word_len);",words)

    connection.commit()

def fetch_max_word_length():
    cursor.execute("SELECT DISTINCT WORD_LENGTH FROM TBL_WORD ORDER BY WORD_LENGTH DESC")
    print(cursor.fetchall())

if __name__ == '__main__':
    insert_word()
    fetch_max_word_length()

