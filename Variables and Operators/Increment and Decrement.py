# Problem Statement
# You must be familiar with various types of operators. One of the most commonly used operators in other languages is increment and decrement operators. Given two numbers X and Y. Your task is to print the value of X decremented by 1 and value of Y after incrementing it by 1.
# Input
# The first line of the input contains two integers X and Y.

# Constraints:
# 1 <= X, Y <= 10000
# Output
# You need to perform the task as mentioned in the question, and finally, print the result separated by a space.
# Example
# Sample Input:
# 4 5

# Sample Output:
# 3 6

# Sample Input:
# 5 6

# Sample Output:
# 4 7



X,Y = list(map(int,input().split()))

X = X-1
Y= Y+1
print(X,Y,end=" ")
