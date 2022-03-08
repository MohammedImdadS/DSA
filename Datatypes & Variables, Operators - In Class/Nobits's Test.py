# Problem Statement
# Nobita wants to score well in his upcoming test, but he is not able to solve the simple division problems, seeing Nobita's determination Doraemon gives him a gadget that can do division problems easily but somehow Nobita deleted the internal program which calculates the division. As an excellent coder, Nobita came for your help. Help Nobita to write a code for his gadget. You will be given two integer D and Q your task is to print the floor value of D/Q.
# Input
# The input contains two space- separated integers depicting the values of D and Q.

# Constraints:-
# 0 <= D, Q <= 100
# Output
# Print the values of D/Q if the value can be calculated else print -1 if it is undefined.

# Note:- Remember division by 0 is an undefined value that will give runtime error in your program.
# Example
# Sample Input:-
# 9 3

# Sample Output:-
# 3

# Sample Input:-
# 8 5

# Sample Output:-
# 1

# Explanation:-
# 8/5 = 1.6 = 1(floor)

D,Q = list(map(int,input().split()))

if(Q==0):
    print(-1)
else:
    div = D//Q
    print(div)
