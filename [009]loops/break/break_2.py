# ask the user for input
questions = ["What is your name?", "Where are you from?", "What is your hobby?"]
n = 0
while True:
    print("Type q to quit")
    answer = input(questions[n])
    if answer == 'q':
        break
    n += 1
    if n > 2:
        n = 0
