def isVowel(character):
    vowels = "aeiou"
    if character in vowels:
        return True
    return False

def vowelSwap(inp):

    # Setting up our pointers and our swap map
    inputLength = len(inp)
    leftPointer = 0
    rightPointer = inputLength - 1
    swapMap = {}

    while leftPointer <= rightPointer:

        # Checking if the left pointer value is not a vowel
        if not isVowel(inp[leftPointer]):
            # If it's not, increment the pointer and continue
            leftPointer += 1
            continue

        # Checking if the right pointer value is not a vowel
        if not isVowel(inp[rightPointer]):
            # If it's not, increment the pointer and continue
            rightPointer -= 1
            continue


        # This only runs when both pointers are at a vowel
        # Recording the swap
        swapMap[leftPointer] = inp[rightPointer]
        swapMap[rightPointer] = inp[leftPointer]

        # Moving pointers to the next value after the swap
        leftPointer += 1
        rightPointer -= 1

    # Create the new string with the swapped vowels
    swappedString = ""
    for i in range(inputLength):
        if isVowel(inp[i]):
            swappedString += swapMap[i]
        else:
            swappedString += inp[i]

    # Return the vowel swapped String
    return swappedString

inputString = "united states"
print vowelSwap(inputString)











