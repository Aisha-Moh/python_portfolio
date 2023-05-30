print("Welcome to my short Harry Potter quiz!")

playing = input("Would you like to play? Yes/No ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's begin")
score = 0

answer = input("1. What is the name of Harry's school? ").lower()
if answer == "hogwarts":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
    score = 0

answer = input("2. What is the name of his headmaster? ")
if answer.lower() == "dumbledore":
    print("Correct! Now for a slightly trickier question...")
    score += 1
else:
    print("Incorrect")
    
answer = input("3. In the Sorcerer's Stone, which animal did Harry have a conversation with at the zoo? ")
if answer.lower() == "snake":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

if score == 0:
    print("Sorry, you scored " + str(score) + " out of 3 questions correct. Try again!")

elif score > 0:
    print("Well done! You got " + str(score) + " out of 3 questions correct.")
    print("That's " + str((score / 3) * 100) + "%!")

