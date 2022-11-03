# You have been given an array A of size N .
# you need to sort this array non-decreasing oder using bubble sort.
# However, you do not need to print the sorted array .
# You just need to print the number of swaps required to sort this array using bubble sort

# Input Format

# The first line consists of a single integer N denoting size of the array. The next line contains N space separated integers denoting the elements of the array.

# Output Format Print the required answer in a single line

# Sample Input
# 5
# 1 2 3 4 5

# Sample Output
# 0

# Standard Bubble Sort is as such:


def bubbleSort(arr):
    index_length = len(arr) - 1
    # this is to optimize the code so that if the array is already sorted it does not have to go through
    # the entire process again.
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# unsorted = [3, 2, 4, 5, 1]
# print(bubbleSort(unsorted))
# works

# So for this specific question, we have to use the inputs

def bubble(arr):
    # n = len(arr)-1
    sorted = False
    count = 0
    while not sorted:
        sorted = True
        for i in range(0, N):
            if arr[i] > arr[i+1]:
                sorted = False
                count = count + 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return count


N = int(input()) - 1
unsorted = list(map(int, (input().split())))

print(bubble(unsorted))
# ans: 0

# this returns us the count of how many swaps are needed to sort this array using bubble sort, which is 0.
