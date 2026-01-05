import random

word_bank = ['Joshua', 'lives', 'with', 'supreme', 'Tunechi']

word = random.choice(word_bank)

guessedWord = ['_'] * len(word)

attempts = 10

while attempts > 0:
    print('\nCurrent word: '+ ''.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great Guess!')
    else:
        attempts -= 1
        print('Wrong guess! You have ' + str(attempts) + ' attempts left.')

    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break

if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)

print('\nThanks for playing!')
