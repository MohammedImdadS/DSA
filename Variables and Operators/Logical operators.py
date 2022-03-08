# Example
# Sample Input:-
# 3 12

# Sample Output:-
# true true true

# Sample Input:-
# 10 10

# Sample Output:-
# true true false


a,b = list(map(int,input().split()))
if a<=10 and b>=10:print("true",end=" ")
else:print("false",end=" ")
if a%2==0 or b%2==0:print("true",end=" ")
else:print("false",end=" ")
if a!=b:print("true",end=" ")
else:print("false",end=" ")
