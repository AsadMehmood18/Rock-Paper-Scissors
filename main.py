import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]
action=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game[action])
print("Computer chose:\n")
rnd = random.randint(0, 2)
print(game[rnd])
if action == rnd:
    print("Draw!")
elif action == 0 and rnd == 2 or action == 1 and rnd == 0 or action == 2 and rnd == 1:
    print("You win!")
else:
    print("You lose!")