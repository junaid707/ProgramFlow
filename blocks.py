name = input("Please enter your name ")
age = int(input("How old are you {}? ".format(name)))
# print(age)

# if age >= 18:
#     print("{}, you are old enough to vote".format(name))
#     print("Please put an X in the box")
# else:
#     print("Hey {0} come back after {1} years".format(name, (18 - age)))

if age < 18:
    print("Come back after {} years".format(18 - age))
elif age == 900:
    print("Sorry, yoda, you die in thr return of the Jedi")
else:
    print("{}, you are old enough to vote".format(name))
    print("Please put an X in the box")



