# Monk loves to preform different operations on arrays, and so being the principal of Hackerearth
# School, he assigned a task to his new student Mishki. Mishki will be provided with an integer
# array A of size N and an integer K, where she needs to rotate the array in the right direction
# by K steps and then print the resultant array. As she is new to the school, please help her to
# complete the task.

# Input:
# The first line will consists of one integer T denoting the number of test cases.
# For each test case:
#     1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
#     2) The next line consists of N space separated integers, denoting the elements of the array A.

# Sample Input
# 1
# 5 2
# 1 2 3 4 5

# Sample Output
# 4 5 1 2 3

t = int(input())
newArr = []

while t != 0:
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    index = n - (k % n)
    for i in range(index, n):
        newArr.insert(len(newArr), arr[i])
    for i in range(index):
        newArr.insert(len(newArr), arr[i])
    t -= 1
    print(*newArr, " ")
