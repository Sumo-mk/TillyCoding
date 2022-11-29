# rock paper scissorcs
# bot generates its move against u
# tells you if you win or lose

from random import randint

Choice = input("Rock paper scissors")
Bot = randint(0,2)
if Bot == 0:
    ValueBot = "Rock"
elif Bot == 1:
    ValueBot = "Paper"
else:
    ValueBot = "Scissors"
print(ValueBot)
if Choice == ValueBot:
    print("Draw")
elif Choice == "Rock" and ValueBot == "scissors":
    print("You Win")
elif Choice == "Paper" and ValueBot == "Rock":
    print("You Win")
elif Choice == "Scisoors" and ValueBot == "Paper":
    print("You Win")
else:
    print("You lose")
