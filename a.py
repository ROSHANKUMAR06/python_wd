# print("https://www.youtube.com/watch?v=nvq9IIW7Tjw&ab_channel=NewsPatra")
# print("\n----------For Login Please------------")
# a=input("Enter Your Name :  ")
# b=input("Your Last Name : ")
# a1=int(input("Your DUCAT ID : "))
# print("Login Successfully........")
# print("\nHello ",a.upper(),b.upper()+"...\n")
# #print("Press")
# print("""Press -
# 1.-> Addition
# 2.-> Subtraction
# 3.-> Multiplication
# 4.-> Division
# 5.-> Square
# 0.-> Exit
# """)
# c=int(input("Enter Your term : "))

# if c==1:
#     print("\n-------------Addition----------------")
#     d=int(input("Enter First no. : "))
#     e=int(input("Enter Second no : "))
#     f=d+e
#     print("Your Sum is : ",f)
#     print("\nThank U Visit Again.....")
#     b1=int(input("Press 0 for exit : "))
#     if b1==0:
#         exit()
# if c==2:
#     print("\n-------------Subtraction-------------")
#     g=int(input("Enter First no. : "))
#     h=int(input("Enter Second no. : "))
#     i=g-h #or h-g
#     print("Your Ans. is : ",i)
#     print("\nThank U Visit Again.....")
#     b1=int(input("Press 0 for exit : "))
#     if b1==0:
#         exit()


# if c==3:
#     print("\n------------Multiplication------------")
#     j=int(input("Enter Your no. : "))
#     k=int(input("Enter Your no. : "))
#     l=j*k
#     print("Your Ans is : ",l)
#     print("\nThank U Visit Again.....")
#     b1=int(input("Press 0 for exit : "))
#     if b1==0:
#         exit()

# if c==4:
#     print("\n-------------Division----------------")
#     m=int(input("Enter Your no. : "))
#     n=int(input("Enter Your no. : "))
#     o=m/n
#     print("Your Ans is : ",o)
#     print("\nThank U Visit Again.....")
#     b1=int(input("Press 0 for exit : "))
#     if b1==0:
#         exit()

# if c==5:
#     print("\n-------------Square.-----------------")
#     p=int(input("Enter Your no. : "))
#     q=int(input("Enter Your no. : "))
#     r=p**q
#     print("Your Ans is : ",r)
#     print("\nThank U Visit Again.....")
#     b1=int(input("Press 0 for exit : "))
#     if b1==0:
#         exit()
# #else:
#  #   print("Not in Range")

# if c==0:
#     exit()

# if c>5:
#     print("Not in Range")


from random import randint
print("welcome to the number guessing game!")
print("i am thinking of a number between 1 and 100")
answer = randint(1, 100)



from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# function to check user's guess against actual answer

def check_answer(guess, answer, turns):
  """check answer against guess. Returns the number of remining."""
  if guess > answer:
    print("too high")
    return turns - 1
  elif guess < answer:
    print("too low")
    return turns - 1
  else:
    print(f"you got it! the number was {answer}.")

# make function to set difficulty
def set_difficulty():
  level = input("choose a difficulty. Type 'easy or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game(): 
  
  # choosing random number betwen 1 and 100 
  print("welcome to the number guessing game!")
  print("i am thing of a number between 1 and 100")
  answer = randint(1, 100)
  print(f"the correct answer is {answer}")
  
  turns = set_difficulty()
  
  
  # repeat the guessing functionality if they get it wrong
  guess = 0
  while guess != answer:
    print(f"you have {turns} attempts remaining to guess the number.")
     

    
    #let the user guess a number
    
    guess = int(input("make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("you have run out of guesses, you lose.")
      return
    elif guess != answer:
      print("guess agin.")




game()