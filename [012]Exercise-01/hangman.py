# Hangman game
# letters_left is the list made of each character in word


def hangman():
    word = "vegetable"
    wrong_guesses = 0
    stages = ["", "_______", "|   |", "|   O", "|  /|\\", "|  / \\", "|      "]
    letters_left = list(word)
    score_board = ['__'] * len(word)
    win = False
    print("Let's play Hangman!")


    while wrong_guesses < len(stages)-1:
        print('\n')
        guess = input("Guess a letter")
        if guess in letters_left:
            char_index = letters_left.index(guess)
            score_board[char_index] = guess
            letters_left[char_index] = '$'
        else:
            wrong_guesses += 1
            print(''.join(score_board))
            print('\n'.join(stages[0: wrong_guesses+1]))
        if '__' not in score_board:
            print('You won!')
            print('The word was: '+ ''.join(score_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose')

hangman()
