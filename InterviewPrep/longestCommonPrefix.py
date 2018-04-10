def longestCommonPrefix(strs):
    if len(strs) < 1:
        return ""
    currentPrefix = strs[0]
    for string in strs:
        tempString = ""
        minLen = min(len(currentPrefix), len(string))
        if len(string) < 1:
            return ""
        for i in range(minLen):
            if currentPrefix[i] == string[i]:
                tempString += string[i]
                if minLen - 1 == i:
                    currentPrefix = tempString
            else:
                currentPrefix = tempString
                break
    return currentPrefix


strs = ["aaabbb","aaabcc","aaab","aaabbbfffeee"]
print longestCommonPrefix(strs)