#coding=utf-8
#---------------------------------------
# 函式名稱: fee
# 傳入參數: (1)是否減價時段, bool 
#           (2)租用分鐘數, int
# 回傳值: (1)費用, int
#---------------------------------------
#(自行完成)
def fee(tfsale,time):
    money=0
    if tfsale == True:
        money = 300 * (time // 60) + 6 * (time % 60)
    else:
        money = 480 * (time // 60) + 9 * (time % 60)
    return money