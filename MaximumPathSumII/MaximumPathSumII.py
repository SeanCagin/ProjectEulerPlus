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