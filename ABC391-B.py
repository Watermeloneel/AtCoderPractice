# 解けなかったのでパス
# # 4 重の for ループによる全探索
# # グリットTを基準として、グリットSのなかで全部一致するものがあるか順番にずらしながらみていくイメージ
# N, M = map(int, input().split())
# S = [input() for _ in range(N)] # N×Nとわかっているので、1行を1つの値として一次元配列に格納
# T = [input() for _ in range(M)] # Sと同様
# print(S)
# print(T)
#
# # 起点となるa,b を固定してループを回し、全部一致するかを判定する
# # a,bの範囲は0からN-M+1まで.0スタートであることに注意
# for a in range(N - M + 1):
#   for b in range(N - M + 1):
#     ok = True
#     for i in range(M):
#       for j in range(M):
#         # print("a + i,b + j=",a + i,b + j)
#         # print("i,j=",i,j)
#         # print("S[a + i][b + j]=", S[a + i][b + j])
#         # print("T[i][j]=", T[i][j])
#         if S[a + i][b + j] != T[i][j]:
#             ok = False
#     if ok:
#       print(a + 1, b + 1)