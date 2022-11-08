# You are given an array of Length N and yoiur task is to check if the array has at least one repeated element in it

# Input

# First line contains a number N (1=<N=<100).
# The next line contains N numbers, the numbers of the first array (1=<Ai=<100).

# Output

# Print "happy" if there is at least one repeated number in the set or "sad" otherwise

# Example 1

# input
# 3
# 1 5 1

# Output

# happy

# Example 2

# input
# 5
# 5 4 3 2 1

# Output

# sad

def happy(arr):
    happySet = set(arr)
    if len(happySet) == len(arr):
        print("sad")
    print("happy")
        
N = int(input())
arr = list(map(int,input().split()))

happy(arr)


# happySort(arr,N)