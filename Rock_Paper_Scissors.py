import random 

user1 = int(input(" 1.ROCK\n 2.PAPER\n 3.SCISSORS.\n "))


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''  print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if user1 == 1:
  print(rock)
  
elif user1 == 2:
  print(paper)

else:
  print(scissors)

print("-----------------------------")

user2 = random.randint(1,3)

print(f"Computer choose {user2}")

if user2 == 1:
  print(rock)

elif user2 == 2:
  print(paper)

else:
  print(scissors)

if user1 == user2:
  print("GAME DRAW")

elif user1 == 1 and user2 == 2:
  print("YOU LOST")

elif user1 == 1 and user2 == 3:
  print("YOU WIN")

elif user1 == 2 and user2 == 1:
  print ("YOU WON")

elif user1 == 2 and user2 == 3:
  print("YOU LOST")

elif user1 == 3 and user2 == 1:
  print("YOU LOST")

else:
  print("YOU WON")