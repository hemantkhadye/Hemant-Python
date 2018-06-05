# =============================================================================
# T=int(input())
# 
# aTime = list(map(int, input().split()))
# bTime = list(map(int, input().split()))
# 
# for i in range(0,T):
#     if aTime[i]==bTime[i]:
#         print("YES")
#     else:
#         print("NO")
#         
# print("")
# =============================================================================


data = "Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, and a syntax that allows programmers to express concepts in fewer lines of code, notably using ..."
spart = data.split()
Dict = {}
for s in spart:
    if s in Dict:
        continue
    else:
        cnt  = data.count(s)
        Dict[] = cnt
print(Dict)