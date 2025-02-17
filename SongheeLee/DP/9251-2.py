import sys
input = sys.stdin.readline

row = input().strip()
col = input().strip()

dp = [[0]*(len(row)+1)]*(len(col)+1)

for j in range(1, len(row)+1):
    for i in range(1, len(col)+1):

        if row[j-1]==col[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1;
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]);

print(dp);

print(dp[-1][-1]);

# S1 = list(input())
# S2 = list(input())
# len1 = len(S1)
# len2 = len(S2)
# dp = [[0]*(len2 + 1) for _ in range(len1+1)]

# for i in range(1,len1 + 1) :
#     for j in range(1,len2 + 1) :
#         if S1[i-1] == S2[j-1] :
#             dp[i][j] = dp[i-1][j-1] + 1
#         else :
#             dp[i][j] = max(dp[i-1][j],dp[i][j-1])

# print(dp[len1][len2])