from m04 import Commission

commissions = []

# 編號, 產品1的銷售金額, 產品2的銷售金額
commissions.append(Commission(1, 300000, 500000))
commissions.append(Commission(2, 200000, 500000))
commissions.append(Commission(3, 100000, 500000))
commissions.append(Commission(4, 80000, 500000))
commissions.append(Commission(5, 300000, 300000))
commissions.append(Commission(6, 200000, 300000))
commissions.append(Commission(7, 100000, 300000))
commissions.append(Commission(8, 80000, 300000))

for c in commissions:
    print('編號:{}, 傭金:{:,.0f}元'.format(c.no, c.total()))