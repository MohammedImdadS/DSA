# Problem Statement
# Given a year, find if it is a leap year. Leap year is the year that is multiple of 4. But, multiples of 100 which are not multiples of 400 are not leap years.
# Input
# User Task:
# Complete the function LeapYear() that takes integer n as a parameter.

# Constraint:
# 1 <= n <= 5000
# Output
# If it is a leap year then print YES and if it is not a leap year, then print NO
# Example
# Sample Input:
# 2000

# Sample Output:
# YES

# Sample Input:
# 2003

# Sample Output:
# NO

# Sample Input:
# 1900

# Sample Output:
# NO
def LeapYear(n):
  if((n % 400 == 0) or (n % 100 != 0) and (n % 4 == 0)):
    return print("YES");
  else:return print("NO");
    
n = int(input())
LeapYear(n)
