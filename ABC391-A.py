# 解法2
D = input()
ans = ""
for d in D:
  if d == "N":
    ans += "S"
  elif d == "S":
    ans += "N"
  elif d == "E":
    ans += "W"
  elif d == "W":
    ans += "E"

print(ans)

# translate関数とmaketrans関数を用いると簡単らしい
# translate →複数の文字を変換, maketrans →文字同士の対応づけ
# def main():
#     s = input()
#     print(s.translate(str.maketrans('NEWS', 'SWEN')))
#
# main()