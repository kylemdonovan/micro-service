import random

def mathinator():
    answer = input("Would you like to generate a random number? (Press 'y' for yes or 'n' for no): ")
    if answer == 'y':

        num = random.randint(0, 1000000)

        #reminder to kyle, change 'w' to 'a' if you want to store the previous number(s) in this file
        f = open("generated_number_file.txt", "w")
        f.write(str(num))
        f.close()

        f = open("generated_number_file.txt", "r")
        print(f.read())

    if answer == 'n':
        return

mathinator()