import keyboard
import random
import os

print("Random question generator. Put your question in ./list.txt.\n")
try:
    f = open('list.txt','r')
    print("Reading file...\n")
except FileNotFoundError:
    print("File list.txt not found. Please create it. Exiting.")
    exit()
else:

        lines = f.readlines()
        f.close()
        if lines == []:
            print("Reached OEF. Exiting.")
            exit()
        max = len(lines)
        ran = False
        print("Type esc for exit or any other for next question.\n")
        i = 0
        j = 0
        while True:
            i = i+1
            j = j+1
            if i > max:
                print("Reached OEF. Repeating.")
                i = 0
            k = input(str(j)+")")
            if k == "esc":
                f.close()
                print("Leaving...\n")
                exit()
            if k == "random":
                ran = not ran
                print(f"Randomness is {ran}")
                i = i-1
                continue
            if(not ran):
                print(lines[i-1])
            else:
                print("-> ")
                print(random.choice(lines))
