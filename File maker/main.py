# File Maker

# Imports
import os
import time

# Code
print("File Maker")
time.sleep(2)
print("By: Den")
time.sleep(3)
print("Version: 1.0.0.0")
time.sleep(2)
while True:
    dirChange = input("Enter your directory to change to: ")
    try:
        os.chdir(dirChange)
        fileMake = input("Enter your file name: ")
        file = open(fileMake, "w")
        writeText = input("Text: ")
        file.write(writeText)
        file.close()
        print("Thanks for using!")
        time.sleep(4)
        break
    except FileNotFoundError:
        print("(!) Directory not found, try again.")
quit()
