# Return the index of first Non Repeating Character
# If the input string does not have any non repeating characters, you should return -1

# Solution 1 - Brute Force
# O(N^2) Time | O(1) Space , N is len of string

def firstNonRepeatingCharacter(string):
    for idx in range(len(string)):
        foundDuplicate = False

        for idx2 in range(len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                foundDuplicate = True

        if not foundDuplicate:
            return idx
    return -1

# Solution 2 
# O(N) Time | O(1) Space because the string contains only 26 alphabets

def firstNonRepeatingCharacter(string):
    charFrequencies = {}
    
    for char in string:
        if char not in charFrequencies:
            charFrequencies[char] = 1
        else:
            charFrequencies[char] += 1

    for char in charFrequencies:
        if charFrequencies[char] == 1:
            return string.index(char)
    return -1

# Solution 3 - Optimal solution
# O(N) Time | O(1) Space because the string contains only 26 alphabets

def firstNonRepeatingCharacter(string):
    charFrequencies = {}

    for char in string:
        charFrequencies[char] = charFrequencies.get(char, 0) + 1
        
    for idx in range(len(string)):
        if charFrequencies[string[idx]] == 1:
            return idx
    return -1