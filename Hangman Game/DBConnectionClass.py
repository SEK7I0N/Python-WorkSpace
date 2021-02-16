import sqlite3
import os
# Create/Connect to DB
#connection =sqlite3.connect("Dictionary.db")

class word:

    

    def __init__(self):
        self.connection =sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()
        #Create Table(s)
        tbl_create_word = """CREATE TABLE IF NOT EXISTS TBL_WORD(
        WORD_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        WORD VARCHAR(100) UNIQUE,
        WORD_LENGTH SMALLINT
        );
        """
        self.cursor.execute(tbl_create_word)
        self.current_Path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def load_words(self):
        with open(os.path.join(self.current_Path, 'words_alpha.txt')) as self.word_file:
            valid_words = set(self.word_file.read().split())

        return valid_words

    def fetch_random_word(self, word_length):
        word_length
        self.cursor.execute(("SELECT * FROM TBL_WORD where word_length = :word_len order by random() limit 1"),{'word_len': word_length})
        word = self.cursor.fetchone()
        return str(word[1])


    def insert_word(self):
        english_words = self.load_words()

        for word in english_words:
            #Insert words into DB with length
            words={'word':word, 'word_len':len(word)}
            self.cursor.execute("INSERT INTO TBL_WORD(WORD, WORD_LENGTH) VALUES(:word, :word_len);",words)
        self.connection.commit()

    def fetch_max_word_length(self):
        self.cursor.execute("SELECT DISTINCT WORD_LENGTH FROM TBL_WORD ORDER BY WORD_LENGTH DESC")
        print(self.cursor.fetchall())
