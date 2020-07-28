# 計算總分的方法
def getSum(scores):
    sum = 0
    for i in range(0, len(scores)):
        sum += scores[i] #累加
    return sum

print(len(scores)) # 數組的元素個數
# 各科列印
for i in range(0, len(scores)):
    print(scores[i])
# 求總分 ?
sum = 0
for i in range(0, len(scores)):
    sum += scores[i] # 累加
print("總分: %d % sum")

# 求平均
avg = sum / len(scores)
print("平均: ")




