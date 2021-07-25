# Validate Subsequence
# A single number from the array is also the valid subsequence of the array

# Solution 1
# Time O(N) | Space O(1)
# Both Solutions are optimal 
def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if sequence[seqIdx] == array[arrIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)

# Solution 2
# Time O(N) | Space O(1)

def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)