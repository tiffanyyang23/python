# 輸入: 一個學生的答案字串(20個字)

# 輸出: 與正確答案比對的結果
#       每個字依序表示該順序的問題是否答對, 若是顯示'.' (小數點), 若否顯示'*' (星號)

# 處理: (1) 如果學生的答案與正確答案相同, 該題就是答對;
#       (2) 如果正確答案是E, 學生答A或B也算對.
#       (3) 如果正確答案是F, 學生答C或D也算對.
#       (4) 不是以上情況之一, 該題就是答錯.
#       (5) 假設標準答案為: EBBDCCCDACBCBADAABCF

w = input("學生答案：")
ans = 'EBBDCCCDACBCBADAABCF'
result = ''
for a in range(len(ans)):
    if ans[a] == 'E':
        if w[a] == ans[a]or w[a] == 'A' or w[a] == 'B':
            result += '.'
        else:
            result += '*'

    elif ans[a] == 'F':
        if w[a] == ans[a]or w[a] == 'C' or w[a] == 'D':
            result += '.'
        else:
            result += '*'
    elif w[a] == ans[a]:
        result += '.'
    else:
        result += '*'

print('正確答案：', ans)
print('比對結果：', result)
