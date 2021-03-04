#coding=utf-8
#--------------------------------------------------------------------
# 函式名稱: credit
# 傳入參數: (1)11個科目的成績, list
# 回傳值: (1)總修課學分, float 
#         (2)總得學分, float
#--------------------------------------------------------------------
# 註:傳入的11個科目的學分依序為:[2, 2, 3, 3, 2, 2.5, 3, 2, 2, 3, 1.5]
def credit(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11):
    c_credit = 0
    g_credit = 0
    sc = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11]
    sc_credit = [2,2,3,3,2,2.5,3,2,2,3,1.5]
    for s in range(len(sc)):
        if sc[s] >= 60:
            g_credit += sc_credit[s]
        if sc[s] == -1:
            c_credit = sum(sc_credit) - sc_credit[s]
        else:
            c_credit = sum(sc_credit)
    return c_credit,g_credit
            