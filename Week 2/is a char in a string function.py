
# Test Case 1
char = "n"; aStr = "abcdefghijklmmopqrstuvwxyz"

def isIn(char,aStr):
    min = 0
    max = len(aStr)
    index = (min+max) //2

    while True:
        if aStr[index] == char:
            return True

        if aStr[index] > char:
            min = index
        if aStr[index] < char:
            max = index

        index = (min + max) // 2
        if (abs(max-min) < 2):
            return False

print (isIn(char,aStr))