# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example 3:

# Input: nums = [3, 3], target = 6
# Output: [0, 1]

# I need two pointers checking if the variables they are pointing to equate to the target sum
# One pointer i starting at index 0 stays while second pointer j starts from index 1 and traverses the rest of the array
# i continues to index 1 with j starting at index 2 and continues

# return index values

# nums = [2, 7, 11, 15]
# target = 9

nums = [3, 2, 4]
target = 6


# O(n^2) solution brute force method
def twoSum(arr, targ):
    list = []
    for i in range(0, len(arr)-1):
        for j in range(1, len(arr)):
            # print(str(arr[i]) + ' - i ,' + str(arr[j]) + ' - j')
            if arr[i] + arr[j] == targ and i != j:
                list = [i, j]
                print(list)
                # print(str(arr[i]) + " + " + str(arr[j]) + " = " + str(targ))
                break


twoSum(nums, target)
# to do
# def improvedTwoSum(arr,targ):
#     list = []
