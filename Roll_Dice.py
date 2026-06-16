import random
import time
print("\033[H\033[J", end="")
roll = random.randint(1,6)
guess = int(input('Guess the diced roll:\n'))

for i in range(10):
    print(".", end="", flush=True)
    time.sleep(0.5)

#print("Waiting for dice to roll :)")
#time.sleep(10)
if guess == roll:
    print("Correct! They rolled a: " + str(roll))
    time.sleep(0.10)
    print("\033[H\033[J", end="")
    print("Try again!")
else:
    print("Wrong!!!! The computer rolled a " + str(roll))
                  