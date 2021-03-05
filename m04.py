# [1] 這家公司的員工負責銷售2種產品 (產品1及產品2), 以下是傭金計算方式:
    
#     [2] 產品1:
#         [2-1] 如果大於(含)300,000元, 有25%傭金率;
#         [2-2] 如果不到300,000元, 但是大於(含)200,000元, , 有20%傭金率;
#         [2-3] 如果不到200,000元, 但是大於(含)100,000元, , 有17%傭金率;
#         [2-4] 如果不到100,000元, 有12%傭金率.
        
#         例如:有員工的[產品1]銷售400,000元, 傭金 = 400,000元 * 0.25 = 100,000元

#     [3] 產品2:
#         [3-1] 如果大於(含)500,000元, 有35%傭金率;
#         [3-2] 如果不到500,000元, 有28%傭金率.
       
#         例如: 有員工的[產品2]銷售300,000元, 傭金 = 300,000元 * 0.28 = 84,000元

#     [4] 員工的傭金 = [產品1]的傭金 + [產品2]的傭金
#         例如: 上述員工的傭金 = 100,000元+ 84,000元 = 184,000元

#佣金，父類別
class Commission():
    
    def __init__(self, no, amount1, amount2):
        self.no = no
        self.amount1 = amount1
        self.amount2 = amount2

    def total(self):
        money_1 = 0
        money_2 = 0
        
        # 計算並回傳傭金
       
        if self.amount1 >= 300000:
            money_1 = self.amount1 * 0.25
        elif 200000 <= self.amount1 and self.amount1 < 300000:
            money_1 = self.amount1 * 0.2
        elif 100000 <= self.amount1 and self.amount1 < 200000:
            money_1 = self.amount1 * 0.17
        else:
            money_1 = self.amount1 * 0.12
        if self.amount2 >= 500000:
            money_2 = self.amount2 * 0.35
        elif self.amount2 < 500000:
                money_2 = self.amount2 * 0.28
        return (money_1 + money_2)