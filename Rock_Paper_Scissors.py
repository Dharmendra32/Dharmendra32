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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
print(game_images[user_choice])
# 0,1,2
Computer_Choice = random.randint(0,2)
print(f"Computer chose:")
print(game_images[Computer_Choice])
if user_choice>= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and Computer_Choice == 2:
    print("You Win")
elif Computer_Choice == 0 and user_choice == 2:
    print("You lose!")
elif Computer_Choice > user_choice:
    print("You Lose")
elif user_choice > Computer_Choice:
    print("You Win!")
elif Computer_Choice == user_choice:
    print("It's a draw")
