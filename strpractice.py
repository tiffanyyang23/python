# 輸入:  由鍵盤輸入一個字串

# 輸出: 字串的總累加分數

# 處理: (1) 輸入字串包括:
#          (1-1) '0' ~ '9' 的數字;
#          (1-2) 'A' ~ 'Z' 的大寫英文字;
#          (1-3) '+' ,  '-' ,  '*' ,  '/' (加減乘除)四種符號.
#          (1-4) 都是半型字, 請別打成全型字
#          (1-5) 假設測試輸入一定符合上述條件, 同學可以不必再檢查輸入字串是否符合條件.

#      (2) 輸入字串可以得到一個 [總累加分數] , 它由字串中的每個字代表之分數累加而成, 計算方法如下:
#          (2-1) 每一個數字, 可得1分;
#          (2-2) 每一個大寫英文字, 可得2分;
#          (2-3) 每一個 '+' (加號) , 可得5分;
#          (2-4) 每一個 '-'  (減號) , 可得5分;
#          (2-5) 每一個 '*' (乘號) , 可得10分;
#          (2-6) 每一個 '/' (除號) , 可得10分;

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     "N", 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
c = ['+', '-', '*', '/']

i = input('請輸入字串：')

cnt_a = 0
cnt_b = 0
cnt_c_12 = 0
cnt_c_34 = 0

for z in i:
    if z in a:
        cnt_a += 1
    if z in b:
        cnt_b += 1
    if z in c:
        if z == '+' or z == '-':
            cnt_c_12 += 1

        if z == '*' or z == '/':
            cnt_c_34 += 1

# 計算得分
score_a = cnt_a*1
score_b = cnt_b*2
score_c12 = cnt_c_12*5
score_c34 = cnt_c_34*10

sum = score_a + score_b + score_c12 + score_c34
print('總累加分數：', sum)
