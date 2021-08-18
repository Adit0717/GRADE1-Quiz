print("WELCOME TO NOOB LEVEL COMPUTER QUIZ")
print("QUIZ CONSISTS OF 5 QUESTIONS, IF YOU GET ALL 5 CORRECT THEN KUDOS!")
print("IF NOT THEN GO BACK TO GRADE 1")
play=input("DO YOU WANT TO PLAY?   A: YES/NO ")

if play.upper() != "YES":
    print("BYE!")
    quit()
    

print("ALRIGHT! LETS PLAY :)")

score=0

#QUESTION 1 
answer = input("WHAT DOES CPU STANDS FOR? ")

if answer.upper() == "CENTRAL PROCESSING UNIT":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")

#QUESTION 2 
answer = input("WHAT DOES GPU STANDS FOR? ")

if answer.upper() == "GRAPHICS PROCESSING UNIT":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")

#QUESTION 3
answer = input("WHAT DOES RAM STANDS FOR? ")

if answer.upper() == "RANDOM ACCESS MEMORY":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")

#QUIESTION 4
answer = input("WHAT DOES ROM STANDS FOR? ")

if answer.upper() == "READ ONLY MEMORY":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")

#QUESTION 5
answer = input("WHAT DOES UPS STANDS FOR? ")

if answer.upper() == "UNINTERRUPTIBLE POWER SUPPLY":
    print("CORRECT")
    score+=1
else:
    print("INCORRECT")

print("YOU GOT "+ str(score) + " QUESTIONS CORRECT")