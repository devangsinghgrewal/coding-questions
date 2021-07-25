# Two Number Sum 
# Take two numbers from the array which will sum to Targetsum , there will only be one such pair
# return empty if no such pair

# Solution 1
# Time O(N) | Space O(1)
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        difference = targetSum - num
        if difference not in nums:
            nums[num] = True
        else:
            return [num, difference]
    return []