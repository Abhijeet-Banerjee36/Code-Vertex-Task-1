# coding project for day 4 
import random
print("\n\n\t WELCOME TO ROCK-PAPER-SCISSOR\t")
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

#Write your code below this line 👇

#      RULES :  rock kills scissors , scissors kills paper , paper kills rock 

#                                    USER INTERFACE 
comp_input=None
Input=int(input("TYPE 0 for rock , 1 for paper , or 2 for scissors  : "))
if Input>=3 or comp_input<0:
    print("you have inputed the invalid number. ")

else:
    print("\t YOUR CHOICE - ")
    choice=[rock,paper,scissors]# TYPE 0 for rock , 1 for paper , or 2 for scissors
    print(choice[Input])
    #                                    COMPUTER INTERFACE     
    print("\t COMPUTER CHOICE -")
    comp_input=random.randint(0,2)
    print(choice[comp_input])

#                                   RESULT INTERFACE 
    if Input==1 and comp_input==0 or Input==2 and comp_input==1 or Input==0 and comp_input==2:
        print("YOU WIN")
    elif Input==comp_input:
        print("it's a DRAW ")
    else:
        print("you Lose ")






 