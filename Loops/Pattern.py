# Problem Statement
# Given an integer N, you have to print the given below pattern for N >= 3.

# Pattern for N = 4:-
# *
# *^*
# *^^*
# *****
# Input
# User Task:
# Since this will be a functional problem, you don't have to take input. You just have to complete the function Pattern() that takes integers N as argument.

# Constraints:-
# 1 <= N <= 100
# Output
# Print the given pattern for size N.
# Example
# Sample input:-
# N = 3

# Sample Output:-
# *
# *^*
# ****

# Sample Input:-
# N = 6

# Sample Output:-
# *
# *^*
# *^^*
# *^^^*
# *^^^^*
# ******

def Pattern(N):
    for i in range(N):
        if i != N-1:
            print("*",end="")
            for j in range(i):
                print("^",end="")
            for k in range(i):
                if k == i-1:
                    print("*",end="")
        if i == N-1:
            for i in range(N+1):
                print("*",end="")

        print("")
