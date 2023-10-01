# We will put the whole structure in an array or arrays.
# This is a tree-like structure but two nodes can share children
# The left child of triangle[i][j] = triangle[i+1][j]
# Similarly, the right child is triangle[i+1][j+1]
# We start adding from the bottom thus only going each element once, making our algorithm O(n)
# Example:
#              3         ->           3       ->      3     ->    23
#            /  \                   /  \            /  \
#           7    4                 7    4          20  19
#         /   \/  \              /   \/  \
#        2    4    6            10   13   15
#       /  \/   \/  \
#      8   5    9   3

t = int(input())  # The number of test cases

for i in range(0, t):
    n = int(input())  # The number of rows the triangle will have
    triangle = []
    for i in range(0, n):
        inputList = input().split()
        for j in range(0, len(inputList)):  # We convert string list to int list
            inputList[j] = int(inputList[j])
        triangle.append(inputList)

    for i in range(n - 2, -1, -1):  # We start from the second to last row and go up
        for j in range(0, len(triangle[i])):
            leftChild = triangle[i+1][j]
            rightChild = triangle[i+1][j+1]
            triangle[i][j] += max(leftChild, rightChild)
    
    print(triangle[0][0])