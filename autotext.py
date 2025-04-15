import time
import keyboard 
 
time.sleep(10)

for line in open("coins.txt", "r"):
    line = '@@@'+line
    for letter in line:
        keyboard.write(letter)