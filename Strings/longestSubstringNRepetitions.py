# String = "aabaaerfsbbcadef"
# Find the longest substring which has no character repeating more than N times

def longestSubstringWithoutDuplication(string, n):
    charCount = {}
    lastSeen = {}
    longest = [0, 1]
    startIdx = 0

    for i,char in enumerate(string):  
        if char in charCount:
            if charCount[char] >= n :
                l = lastSeen[char][charCount[char] - n]
                startIdx = max(startIdx, l + 1)

        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]

        charCount[char] = charCount.get(char, 0) + 1

        if char not in lastSeen:
            lastSeen[char] = [i]
        else:
            lastSeen[char].append(i)
    return string[longest[0]: longest[1]]

# Test Case
print(longestSubstringWithoutDuplication("aabaaerfsbbcaadef", 2) == "erfsbbcaadef")