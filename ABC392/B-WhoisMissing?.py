N, M = map(int, input().split())
Alist = list(map(int, input().split()))
Ans = []

# M無くても良さそうだけど一応
if not len(Alist) == M:
    quit()

for i in range(1,N+1):
    if not i in Alist:
        Ans.append(i)

if len(Ans) == 0:
    Ans.append(0)

print(*Ans) # 配列の中身を取り出す方法