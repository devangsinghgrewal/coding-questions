# Write a function that takes in non-empty string and return it's run length encoding

# Worst -Time 2O(N) --> O(N) | Space O(2N) --> O(N)

def runLengthEncoding(string):
    chars = []
    length = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1] and length != 9:
            length +=1
        else:
            chars.append(str(length))
            chars.append(string[i - 1])
            length = 1
    # Hand the last case
    chars.append(str(length))
    chars.append(string[len(string) - 1])
    return "".join(chars)