print("Welcome to my baseball quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play. When typing a name, use both first and last name :)")
score = 0

answer = input("Who has the most home runs all time? ")
if answer.lower() == "barry bonds":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who has the most hits all time? ")
if answer.lower() == "pete rose":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the number of most home runs in a season? ")
if answer.lower() == "73":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the number of most hits in a season? ")
if answer.lower() == "262":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who has the most strikeouts all time? ")
if answer.lower() == "nolan ryan":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
