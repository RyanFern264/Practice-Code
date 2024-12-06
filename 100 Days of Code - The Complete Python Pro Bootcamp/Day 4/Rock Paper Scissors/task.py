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
print("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors")
player_choice = int(input())
options = [rock, paper, scissors]
npc_choice = random.randint(0, 2)
print(options[player_choice])
print("Computer chose:\n")
print(options[npc_choice])

if player_choice == 0:
    if npc_choice == 0:
        print("Draw")
    if npc_choice == 1:
        print("You lose")
    if npc_choice == 2:
        print("You win!")
elif player_choice == 1:
    if npc_choice == 0:
        print("You win!")
    if npc_choice == 1:
        print("Draw")
    if npc_choice == 2:
        print("You lose")
elif player_choice == 2:
    if npc_choice == 0:
        print("You Lose")
    if npc_choice == 1:
        print("You win!")
    if npc_choice == 2:
        print("Draw")
else:
    print("Please pick a valid number")
