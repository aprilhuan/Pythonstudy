import random

while True:
    n = random.randint(1, 100)
    # 若 n 等於3的倍數才印出
    if n % 3 == 0:
        print(n)
    # 若 n 等於11的倍數就停止 (break)
    if n % 11 == 0:
        break
