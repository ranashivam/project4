print("Welcome to my comouter quiz!")

playing = input("Do you want to play? (Yes/No)")

score = 0

if playing.lower() != "yes":
    quit()

print("Let's start the game")

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!!!!!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!!!!!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!!!!!")

answer = input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!!!!!")

totalScore = print("Your total score is: ", score)