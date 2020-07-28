report = "台積電目前價格315.5元,非常適合買進4000股, 目前我的庫存有6000股"
# 求賣出後的庫存總值 ?
price = float(report[5:10])
amount = int(report[5:19])
stock = int(report[28:32])
print(price, amount, stock)
print(price * (stock-amount))


