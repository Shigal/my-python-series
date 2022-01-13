'''
 Write a program that has an infinite loop (with q to quit),
 and each time through theloop, it asks the user to guess a number
 and tells them whether their guess was right or wrong
'''

num = [10, 23, 45, 12]

while True:
    value = input('Guess a number or type q to quit')
    if(value == 'q'):
        break
    try:
        value = int(value)
    except ValueError:
        print("Please type a number or type q to quit")
    if value in num:
        print("Guess is right")
    else:
        print("Guess is wrong")
