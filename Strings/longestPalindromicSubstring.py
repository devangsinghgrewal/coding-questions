# Write a function that given a string return its Longest Palindromic Substring
# Assume there is only one Longest Palindromic Substring

# Solution 1 - Brute Force
# Time O(N^3) | Space O(N)
from palindrome import isPalindrome

def longestPalindromicSubstring(string):
    longest = ""
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i : j + 1]
            if len(substring) > len(longest) and isPalindrome(substring):
                longest = substring
            if len(longest) == len(string) - i:
                return longest
    

# Solution 2 - Optimal
# Time O(N^2) | Space O(N). N is the len of string
# It's true that throughout our traversal of the input string, 
# we only store an array of length 2; however, we ultimately still need to slice the longest
#  palindromic substring out of the string, and this longest palindromic substring can be as 
#  large as the string itself, in the worst case.

Thus, the algorithm runs with linear space
def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0] : currentLongest[1]] 

        
def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]


# Test Cases
# Should Return True
print(longestPalindromicSubstring("it's highnoon") == "noon")
print(longestPalindromicSubstring("abcdefghfedcbaa") == "aa")