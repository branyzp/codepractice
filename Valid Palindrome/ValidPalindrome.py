# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

# first method using python methods
# def isPalindrome(s):
#     # create new string and add a char into new string if it is alphanumeric (aA -zZ, 0-9) in lowercase
#     newS = ""
#     for char in s:
#         if char.isalnum():
#             newS += char.lower()

#     # return boolean value of if new string is the same backwards
#     return newS == newS[::-1]


# second method (2 pointers at each end)
def isPalindrome(s):
    l, r = 0, len(s)-1

    while l < r:
        while l < r and s[l].isalnum() == False:
            l += 1
        while r > l and s[r].isalnum() == False:
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l+1, r-1
    return True


s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))
