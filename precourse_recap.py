age_guess = int(input("Guess what age Michael is: "))
age_actual = 39

if age_guess == 39:
    print("Bingo! You are correct.")
elif age_guess > 46:
    print("Oh come on! Lockdown must've really aged me!")
elif age_guess >= 35 and age_guess <= 45:
    print("Close enough, Michael is " + str(age_actual))
elif age_guess < 34:
    print("Thanks very much, I'm due you a beer.")