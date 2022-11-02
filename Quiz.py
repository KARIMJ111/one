import time

print("Welcome to my quiz!")

playing = input("Would you like to play? ").lower()
if playing != "yes":
    quit()
else:
    print("Okay! Lets play!")
score = 0

playing = input("What is the capital of Ireland? ").lower()
if playing == "dublin":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

playing = input("What does CPU stand for? ").lower()
if playing == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

playing = input("How many states make up the USA? ").lower()
multi_choice = ['fifty', '50']
if playing in multi_choice:
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print('End of quiz.')
time.sleep(1)
print("You got " + str(score) + " out of 3 questions correct!")
perc = str(score / 3 *100)
print("Meaning you got " + perc + "%")
time.sleep(1)
if perc == '100.0':
    print("Well Done!")
else:
    print("Better luck next time!")