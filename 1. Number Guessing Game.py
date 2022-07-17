import random
n = random.randrange(1, 100)
guess = int(input('Enter the number: '))
while n!= guess:
    if guess < n:
        print("Too Low!")
        guess = int(input('Enter the higher number: '))
    elif guess > n:
        print("Too High!")
        guess = int(input('Enter the lower number: '))
    else:
        break
print("You guessed it Right")