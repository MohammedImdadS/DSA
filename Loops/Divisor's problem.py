# Problem Statement
# Sara is solving a math problem in which she has given an integer N and her task is to find the number of operations required to convert N into 1.
# Where in one operation you replace the number with its second-highest divisor.
# Input
# User Task:
# Since this will be a functional problem, you don't have to take input. You just have to complete the function DivisorProblem() that takes integer N as argument.

# Constraints:-
# 1 <= N <= 100000
# Output
# Return the number of operations required.
# Example
# Sample Input:-
# 100

# Sample Output:-
# 4

# Explanation:-
# 100 - > 50
# 50 - > 25
# 25 - > 5
# 5 - > 1

# Sample Input:-
# 10

# Sample Output:-
# 2

def DivisorProblem(N):

  initial = N
  suming = 0
  i = 0
  while i!=1:
    divisor = SecHigh_Div(initial)
    initial = divisor
    i = divisor
    suming += 1
  return suming
  

def SecHigh_Div(N):
  List = []
  for i in range(N):
    ivalue = i+1
    if N % (ivalue) == 0:
      List.append(ivalue)
  secHigh = List[len(List)-2]
  # print("second highest divisor = {}".format(secHigh))
  List.clear()
  return secHigh
