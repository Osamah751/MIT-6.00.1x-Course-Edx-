def middle(min, max):
    num = (min + max)//2
    return num

print('Please think of a number between 0 and 100!')

min = 0
max = 100
num = 50
answer = None
print('Is your secret number ' + str(num) + ' ?')

while answer!= "c":
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if answer == "h":
        max = int(num)
        num = int(middle(min, num))

    elif answer == "l":
        min = int(num)
        num = int(middle(num, max))

    elif answer == "c":
        print('Game over. Your secret number was:', str(num))
        break
    else:
        print("Sorry, I did not understand your input.")
    print('Is your secret number ' + str(num) + ' ?')

#---------------------