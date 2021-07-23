# Write a function that takes in non-empty string and return a boolean whether string is Palindrome
# or not 

# Time Complexity - O(N)
# Space Complexity - O(1)
def isPalindrome(string):
    leftIdx = 0
	rightIdx = len(string) - 1
	while leftIdx < rightIdx:
		if string[leftIdx] != string[rightIdx]:
			return False
		leftIdx += 1
		rightIdx -=1

	return True 
