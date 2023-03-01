#quiz game
print("Welcome to the Bridge of Death")

playing = input("Do you want to cross? ")


if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

print("Question 1")

questionOne = input("What is the capital of Assyria? ")

if questionOne.lower() != "Assur":
        quit("You are cast into the gorge of eternal peril :( )")
        score += 1
print("You live for now! Next Question! ")

questionTwo = input("Who was the first US President? ")

if questionTwo.lower() != "George Washington":
    quit("You are cast into the gorge of eternal peril :( )")
    score += 1
print("Good job! One more question ")


questionThree = input("What book is the third installment of Twilight? ")

if questionThree.lower() != "Eclipse":
    quit("You have been thrown into the abyss :( )")
    score += 1
print("You have answered correctly! You may pass over the gorge of eternal peril :) ")

print("You got " + str((score / 4) * 100) + " questions correct!")