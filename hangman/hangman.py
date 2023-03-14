from words import words
import random
lives = 6


def random_word():
    word = random.choice(words).lower()
    return word


random_word = random_word()
word = ['_'] * len(random_word)
user_letters = []


game_over = False


while game_over == False:
    print(random_word)
    if "".join(word) == random_word:
        print(f'you win, good guess {random_word} ')
        break
    print(word)
    print(lives)

    user = input('Please type a letter: ').lower()

    if lives == 1:

        print('gameover')
        break

    elif user not in random_word and user not in user_letters:

        lives -= 1

    if user not in user_letters:
        for letter in range(len(random_word)):
            if user in random_word[letter]:

                word[letter] = user
                user_letters.append(user)

    else:
        print('you have used that letter already')
