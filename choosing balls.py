"""

There are N balls in a row numbered 1 to N from left to right. For each ball i, Bi represents its size. You are initially on the leftmost ball (ball number 1). You can make an arbitrary number of choices (including zero) as long as the following conditions are satisfied:

1. You can only choose a ball which is next to the current ball i.e. from ith ball, you can choose i+1th ball i.e. next right (if exists).

2. It’s always possible to choose a ball with the same size as the current ball.

3. It’s possible to choose a ball if its size is larger than the current ball by no more than U.

4. It’s possible to choose a ball if its size is smaller than the current ball by no more than D.

5. You have one special choice where you can choose a smaller ball regardless of its size (as long as it is smaller than the current ball). This choice is available at most one time.


Your task is to choose the highest indexed ball. Determine the index of the rightmost ball you can reach.

Input Format:

The first line of the input contains three space-separated integers N, U, and D

The second line contains N space-separated integers B1, B2, …, BN.

Output Format:

Print a single line containing one integer -- the index of the rightmost reachable ball.

Constraints:

1<= N <=100
1<=U, D<=1,00,000
1<= Bi <=1,00,000

Example:

Input:
5 3 2
2 5 2 6 3

Output:
3


"""


N,U,D = map(int, input().split())
B = list(map(int, input().split()))
s = True
c = 0
for i in range(0,N-1):
  if B[i] == B[i+1]:
    c += 1
  if B[i] < B[i+1]:
    if((B[i+1] - B[i]) <= U):
      c += 1
    else:
      break
  if B[i] > B[i+1]:
    if((B[i+1] - B[i]) <= U):
      c += 1
    elif(s):
      c += 1
      s = False
    else:
      break
print(c + 1, end =" ")
