# coding=utf-8
# -------------------------------
# 函式名稱: score
# 傳入參數: (1)第1次分數, int
#           (2)第2次分數, int
#           (3)第3次分數, int
#           (4)第4次分數, int
#           (5)第5次分數, int
# 回傳值: (1)等第總分, float
# -------------------------------
# (自行完成)


def score(exam1, exam2, exam3, exam4, exam5):
    sc = [exam1, exam2, exam3, exam4, exam5]
    rantsum = []
    for s in sc:
        if s >= 90 and s <= 100:
            rantsum.append(4.3)
        elif s >= 85 and s <= 89:
            rantsum.append(4.0)
        elif s >= 80 and s <= 84:
            rantsum.append(3.7)
        elif s >= 77 and s <= 79:
            rantsum.append(3.3)
        elif s >= 73 and s <= 76:
            rantsum.append(3.0)
        elif s >= 70 and s <= 72:
            rantsum.append(2.7)
        elif s >= 67 and s <= 69:
            rantsum.append(2.3)
        elif s >= 63 and s <= 66:
            rantsum.append(2.0)
        elif s >= 60 and s <= 62:
            rantsum.append(1.7)
        elif s >= 0 and s <= 59:
            rantsum.append(0)
    return sum(rantsum)
