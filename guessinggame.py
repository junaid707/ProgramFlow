answer = 5

print("Please guess between 1 to 10: ")
guess = int(input())

if guess == answer:
    print("You've got it at first")
else:
    if guess < answer:
        print("guess high")
    else:
        print("Guess low")
    guess = int(input())
    if guess == answer:
        print("well done, you got it")
    else:
        print("Sorry you have not got it")

# if guess != answer:
#     if guess < answer:
#         print("Guess higher number")
#     else:
#         print("Guess low number")
#     guess = int(input())
#     if guess == answer:
#         print("You've guessed it correctly")
#     else:
#         print("Sorry, you have not guesses correctly")
# else:
#     print("You have got it first time")

# if guess < answer:
#     print("Please guess high")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it well done")
#     else:
#         print("sorry, you've not guesses correctly")
# elif guess > answer:
#     print("Please guess low")
#     guess = int(input())
#     if guess == answer:
#         print("You guessed it well done")
#     else:
#         print("sorry, you've not guesses correctly")
# else:
#     print("You've guessed correctly")
