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

# 別の解法メモ
# バケットソートの要領で解く方法
# 1. 要素数Nで値がすべて0の配列を用意
# 2. A を for文で回しながら1つずつ取得、要素数とAの値がイコールの場合、値を1に変更
# 3. 最後に配列が0の要素数を出力