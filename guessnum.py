import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Incorrect! Whadda heeeiill?? Guess is low. Try high.')
        elif guess > random_number:
            print('Incorrect! Are you high?? Guess is high. Try lower.')
        
    print(f'Hee... Hee... Your guessed the number {random_number}')
    
guess(20)