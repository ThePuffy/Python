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

l = [rock, paper, scissors]
que = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(l[que])