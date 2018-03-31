

def deleteReoccurringCharacters(string):
    seenCharacters = set()
    outputString = ''
    for char in string:
        if char not in seenCharacters:
            seenCharacters.add(char)
            outputString += char
    return outputString


inputString= "aabbccc anthony"
print deleteReoccurringCharacters(inputString)