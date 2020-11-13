# do exercise
var = input("Enter your name\n")
print("hello,", var)
n = 12
number_of_guesses = 1
print("You have only 9 guesses\n")
while number_of_guesses <= 9:
    guess_number = int(input("Guess the number :\n"))
    if guess_number > 12:
        print("You have entered greater no. please enter less no:\n")

    elif guess_number < 12:
        print("You have entered smaller no. please enter larger no:\n")
    else:
        print("You won!")
        print(number_of_guesses, "number of guesses took to finish")
        break
    print(9 - number_of_guesses, "number of guess left\n")
    number_of_guesses = number_of_guesses + 1

if number_of_guesses < 9:
    print("Game Over")










