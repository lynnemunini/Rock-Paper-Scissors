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
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors. "))
      
choices = [rock, paper, scissors]
value = random.randint(0,2)
print("\n\nComputer chose:")
print(choices[value])
print("You chose")
print(choices[choice])
if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
elif choices[choice] == choices[value]:
  print("It's a Draw")
elif choices[choice] == rock and choices[value] == scissors:
  print("You win👒")
elif choices[choice] == scissors and choices[value] == paper:
  print("You win👒")
elif choices[choice] == paper and choices[value] == rock:
  print("You win👒")
elif choices[value] == rock and choices[choice] == scissors:
  print("You Lost")
elif choices[value] == scissors and choices[choice] == paper:
  print("You Lost")
elif choices[value] == paper and choices[choice] == rock:
  print("You Lost")

  