def calc(x=1, y=2) -> int :
    return x + y

def calc(x=None, y=None) -> int :
    if x == None:
        print('使用者沒帶入X值')
    return x + y

if__name__
    sum = calc(10, 20)
    print(sum)
    sum = calc()
    print(sum)
    sum = calc(7)
    print(sum)
    sum = calc(y=7)
    print(sum)







sum = calc2(6)
