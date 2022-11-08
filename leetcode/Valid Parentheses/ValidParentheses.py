# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# Hashmap and stacks
def isValid(s):
    stack = []
    hashMap = {")":"(",
               "]":"[",
               "}":"{"}
    for c in s:
        # keys are closing parentheses
        if c in hashMap:
            # make sure stack is not empty and value at top of stack (last added) match the parenthesis in the hashmap
            if stack and stack[-1] == hashMap[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False




s = "()"

print(isValid(s))
