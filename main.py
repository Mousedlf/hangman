word = "musical"
word_as_list = list(word)

hidden_word = "_" * len(word)
hidden_word_as_list = list(hidden_word)

wrong_guesses = []

def hangman_ascii():
    if len(wrong_guesses) == 0:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif len(wrong_guesses) == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif len(wrong_guesses) == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif len(wrong_guesses) == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif len(wrong_guesses) == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif len(wrong_guesses) == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    else:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")
        print("you dead")


def test():
    print(hidden_word)
    guess = input("your letter : ").lower()
    if guess in word:
        print('yey')
        found_letter_index = word_as_list.index(guess)  # fonctionne pas si 2 occurences dans mot
        hidden_word_as_list[int(found_letter_index)] = guess
        print(' '.join(hidden_word_as_list))
    else:
        print('nope')
        wrong_guesses.append(guess)
        hangman_ascii()

    print(wrong_guesses)
    test()


test()
