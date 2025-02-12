a1, a2, a3 = map(int, input().split())
if a1 * a2 == a3 or a2 * a3 == a1 or a3 * a1 == a2:
    print("Yes")
else:
    print("No")

# 大小関係を利用した解法
# A = list(map(int, input().split()))
# A.sort()
# print(A[0], A[1], A[2])
# if A[0] * A[1] == A[2]:
#     print("Yes")
# else:
#     print("No")