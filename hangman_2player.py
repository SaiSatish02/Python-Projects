import getpass
import time
import os
print("HELLO HOST!!")
name=input("Enter your name:")
print("EASY MODE: Set 1 words are about fruits ")
print("MEDIUM MODE: Set 2 words are about Unicorns(Tech Giants)")
print("HARD MODE: Set 3 words are about scientists")
sett=int(getpass.getpass("Enter the set number:"))
if sett==1:
    secret = getpass.getpass(name+ ",Enter the secret word:")
elif sett==2:
    secret = getpass.getpass(name+" ,Enter the secret word:")
else:
    secret = getpass.getpass(name+" ,Enter the secret word:")
time.sleep(2)
os.system("clear")


name2=input("Enter the name of person who is playing:")
print("WELCOME TO HANGMAN GAME!!! \n",name2)
print("Your task:--  Guess the hidden word given by your opponent.\n")
print("Your hint is:")
if sett==1:
    print("HINT:Word is about fruits!!")
    
elif sett==2:
    print("HINT:Word is about Unicorns(tech giants)!!")

else:
    print("HINT:Word is about scientists!!")


display=["_"]*len(secret)
print(display)
chances=len(secret)+2
print(" Your total number of chances to guess the word are:",chances)
com=list(secret)
count=1
while 1:
    flag=False
    if count>chances:
        print("You lost the game\n")
        print("The correct word is ",secret)
        break
    char=input("Guess the letter:").lower()
    if char.isdigit():
        print("Your choice is wrong.Enter only letters\n")
        continue
    if len(char)>=2:
        print("Dont enter string .Enter only single letter at a time\n")
        continue
    
    for i in range(len(secret)):
        if char==secret[i]:
            display[i]=char
            flag=True
    if  not flag:
        print("You guessed wrong letter. No problem try to guess in next chance ",name)
        chances=chances-count
    print(display)
    if display==com:
        print("Congratulations!!!.\nYou guessed the word correctly!!!!\n")
        break
    print("The total number of chances left are ",chances)
        