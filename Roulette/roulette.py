# roulette
import random
print("Welcome to Martin Pangelov CASINO!")
print("You are playing roulette")
print("----------------------------------------------")
print("Entry plot: ")
entry_plot = float(input())

while entry_plot > 0:
    print("Enter your bet: ")
    bet = float(input())
    if bet <= entry_plot:
        print("Enter the number you want to bet on: ")
        enter_number_you_want_to_bet_on = int(input())
        random_number = random.randint(1, 37)
        if enter_number_you_want_to_bet_on == random_number:
            entry_plot = entry_plot + (bet * 36)
        else:
            entry_plot = entry_plot - bet
        print(f"Actual sum: {entry_plot}")
    else:
        print("Your bet is bigger than the balance!")
        continue
print("Your money finished!")



