# Problem Statement
# Given an integer n, your task is to print a right angle triangle pattern of consecutive numbers of height n.

# eg:-

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Input
# User Task:
# Since this will be a functional problem, you don't have to take input. You just have to complete the function pattern() that takes integer n as a parameter.

# Constraint:
# 1 <= n <= 100
# Output
# Print a right angle triangle of numbers of height n.
# Example
# Sample Input:
# 5

# Sample Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# Sample Input:
# 2

# Sample Output:
# 1
# 1 2


def patternPrinting(N):
    for i in range(N):
        for j in range(N):
            if j==i+1:break
            print(j+1,end =" ")
        print("")
