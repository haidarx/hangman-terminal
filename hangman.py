import textwrap
import time
import os
import sys
import random

import lives
import getcharacter

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

listWord= []
try:
    with open("wordlist.txt") as file:
        for line in file:
            listWord.append(line.rstrip())

except Exception as e:
    print("Caught Exception: \n",e)
    print("\nCaught error during loading of the word list. Using default minimal list...")
    listWord = ["potato", "automobile", "hippopotamus", "binary"]

def inputChar():
    b = getcharacter.getch()
    c = b.decode("utf-8")
    return c

def generateUnderscore(inputStr):
    st= []
    for i in inputStr:
        st.append("_")
    return st 

def replaceUnderscore(guess, question, outputList):
    for index, val in enumerate(question):
        if guess == val:
            outputList[index] = val

def restartPrompt():
    yesList = ["y","yes", "yeah"]
    noList = ["n", "no", "non", "not","nope", "exit", "quit", "q"]
    while True:
        choice = input("Would you like to play? [y/n]: ")
        if choice.lower() in yesList:
            break
        elif choice.lower() in noList:
            print("Bye. Thanks for playing!")
            sys.exit(0)
        else:
            print("Try again")
            continue
        return

def gameMain():
    while True:
        restartPrompt()
        questionWord = random.choice(listWord)
        outputList = generateUnderscore(questionWord)
        usedChar = []
        currentLives = 6

        while True:
            lives.drawLives(currentLives)
            print(f"Guess the Word!")
            print(" ".join(outputList))
            print(f"Current Lives: {currentLives}")
            print(f"Used characters: {usedChar}")

            if "_" not in outputList:
                print("YOU WIN!")
                time.sleep(3)
                break
            if currentLives == 0:
                print("YOU LOSE!")
                time.sleep(3)
                break

            # TO DO= Parse first
            # print("Your guess? ")
            # c = inputChar()
            
            c = input("Your guess? ")
            
            # print(CURSOR_UP_ONE + ERASE_LINE)

            if c in usedChar:
                print(f"Character {c} is already used! -1 Live")
                currentLives -= 1
                
            elif c in questionWord:
                print("Correct guess!") 
                replaceUnderscore(c, questionWord, outputList)
                usedChar.append(c)
                

            else:
                print("Wrong guess!")  
                usedChar.append(c)
                currentLives -= 1
            
            time.sleep(1)

    return



if __name__ == "__main__":
    # Test Lives Import
    
    # test = lives.drawLoop(6)
    # test.draw()
    # test.reverse()
    
    
    gameMain()