"""
author: SEK7I0N

"""
import DBConnectionClass



def get_input_from_user():
    #getting input from the user for number_of_tries and word_length 
    while True:
        number_of_tries = int(input("Select number of attempts[3-25] "))
        if 3 <= int(number_of_tries) <= 25:
                break
        print("Please enter a number in range of 3-25")
    while True:
        word_length = int(input("how lengthy of a word do you want[3-25]? "))
        if 3 <= int(word_length) <= 25:
                break
        print("Please enter a number in range of 3-25")
    return (number_of_tries, word_length)
        
def play_hangman():
    obj_word = DBConnectionClass.word()
    obj_word.insert_word()
    while True:
        number_of_tries, word_length = get_input_from_user()
        #Fetching a random word from the Table with required length
        word = obj_word.fetch_random_word(word_length)
        flag = False
        word_guess = '*' * word_length
        
        while number_of_tries != 0:
            char_for_word = input("input character for the word:")
            word_guessed = ''
            if char_for_word in list(word):
                for word_index in range(0, word_length):
                    if word[word_index] == char_for_word:
                        word_guessed.add(char_for_word)
                    else:
                        word_guessed.add('*')

            if word == word_guess:
                flag = True
                break
            number_of_tries = number_of_tries - 1
        print("Horray!! you guessed the correct word: {0}".format(word_guess))
        answer = str(input("DO you wanna guess another word?[Y/N]? "))
        if answer in ('y','n','Y','N'):
            break
    
if __name__ == '__main__':

        play_hangman()
