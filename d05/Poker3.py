import random
import time

def getScore(p):
    if p == 'A':
        return 1
    elif p == 'J' or p == 'Q' or p =='k':
        return 0.5
    return p # 2-10的數字

poker = 6
poker = ["A" , 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
random.shuffle(poker)  # 洗牌

# 餘額(目前金額)
balance = 100

while True:
    # 下注
    bet = int(input('請下注(不可超過 %d), 離開:-1: ' % balance))


print(poker)
p1 = poker.pop()
sum = getScore(p1)
print('已拿:', p1, '總分:', sum)
print('剩餘:', poker)


    bet = int(input('請下注(不可超過 %d), 離開:-1: ' % balance))
    if bet == -1:

# 繼續拿牌?
count_user = 0
while True:
    ask = input('是否要拿牌(y/n)? ')
    if ask == 'y':
        p = poker.pop()
        sum += getScore(p)
        print('再拿:',p , '總分:', sum)
        if sum > 0.5:
            print('user爆了')
            break
        else:
            count_user += 1
        if count_user == 5:
            print('user 過五關, 超強的~~~')
            break
        else:
            break







    # PC 拿牌
    count_pc = 0
    p2 = poker.pop








































    # sum, count_pc
    if count_user == 5 and sum <= 10.5:
        balance += bet
        print('User 贏, 最新餘額:', balance)
        continue # 進入下一局
    if (sum > 10.5 and sum2 > 10.5) or (sum == sum2):
        print('和局, 最新餘額:', balance)
        continue # 進入下一局



















while True:
    if sum >= 9:
        break
    elif sum < 7:
        p = poker.pop()
        sum += getScore(p)
        print('pc再拿:')
p2 = poker.pop()
sum = getScore(p2)
print('PC已拿:', p2, "總分:", sum)
print('剩餘:' 0




print(poker,count)








# 繼續拿牌 ?
while True:
    ask = input('是否要拿牌(y/n)? ')
    if ask == 'y':
        p = poker.pop()
        sum += sum + getScore(p)
        print('再拿:' + p, '總分:', sum)
    else:
        break