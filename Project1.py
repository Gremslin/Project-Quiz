print("Welcome to Project Quiz!")

while True:
    play = input(".Type 1 for playing \n.Type 2 for leaving \n")
    try:
        if int(play)==1:
            break
        if int(play)==2:
            quit()
    except ValueError:
        print("\nVery funny, please enter a valid option:\n")

user = input("\nAwesome! So, What's your name?\n")
print("\nPerfect " + str(user) + ", the rules are simple:\n \nQuestions are gonna appear in the screen and you have to type the answer \nIf your answer is correct +1 point \nIf you answer is incorrect -1 point")
input("\nPress enter to start")
score = 0
answer = input("\n1. How many colors are in the visible spectrum? \n")
if int(answer) == 7:
    print("Correct!")
    score += 1
else:
    print("Nope, Incorrect!")
    score -= 1

answer = input("\n2. How many bone does an adult human skeleton have? \n")
if int(answer) == 206:
    print("Correct!")
    score += 1
else:
    print("Nope, Incorrect!")
    score -= 1

answer = input("\n3. In which year did the covid-19 pandemic start? \n")
if int(answer) == 2020:
    print("Correct!")
    score += 1
else:
    print("Nope, Incorrect!")
    score -= 1

if int(score)<0:
    fscore = 0
else:
    fscore = score

if fscore == 0:
    print("\nTime to study " + str(user) + ", your final score is: " + str(fscore))
else:
    print("\nNice " + str(user) + "! Your final score is: " + str(fscore))

print("\nThanks for playing " + str(user) + "! Press enter to close the game")
if input():
    quit()
