# Problem Statement
# Sara is standing in a line for her turn to see the doctor. There are N people standing in front of Sara and for each person, the doctor takes exactly X minutes. Sara wants to know the time after which her number comes. Since Sara is weak in maths, your task is to calculate the time for her.
# Input
# Th input contains two integers N and X.

values = list(map(int,input().split()))

for i in values:
    N = values[0]
    X = values[1]
    turn = N * X
print(turn)
