import random
ans = random.randint(1, 99)
min, max = 0, 100
while amount > 0:
    amount -= 1
    iguess = input('請在%d~%d之間猜一個數字:' % (min, max))
    # 驗證範圍 ?
    if guess <= min or guess >= max:
        print('輸入範圍錯誤, 請重新輸入')
        continue
    # 是否猜對 ?
    if guess > ans:
        max = guess
    elif guess < ans:
        min = guess
    else:
        print('恭喜答對了')
        break


    # 若都沒有猜對
    if amount == 0:
        print("GG了 , 答案:", str(ans))











