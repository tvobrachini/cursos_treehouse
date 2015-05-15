import random


random_number = random.randint(1, 10)
guessed_numbers = list()
max_guesses = 5

while len(guessed_numbers) < max_guesses:
    guess = input("Hey you! Tell me a number between 1 and 10: ")

    try:
        player_num = int(guess)
    except:
        print("That's not a hole number!")
        break

    if not player_num > 0 or not player_num < 11:
        print("That number is out of the range [1..10]")
        break

    guessed_numbers.append(player_num)

    if player_num == random_number:
        print("You won!! My number was {}!".format(random_number))
        print("It took you {} tries to get that right".format(
            len(guessed_numbers)))
        break
    else:
        if player_num > random_number:
            print("Nope! Too hight!")
            print("You still have {} more shots!".format(
                max_guesses-len(guessed_numbers)))
        if player_num < random_number:
            print("Nope! Too Low!")
            print("You still have {} more shots!".format(
                max_guesses-len(guessed_numbers)))

        continue

if random_number not in guessed_numbers:
    print("Sorry! Maybe try it again later!")
    print("BTW my number was {}".format(random_number))
