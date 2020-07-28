def calc(x, y):
    a = 2 * x
    b = y - a
    rabbit = b / 2;
    return x-rabbit, rabbit

chicken, rabbit = calc(101, 240)
print("雞:%d 兔:%d 5 隻數:%d  ")


chicken, rabbit = calc(83,240)
print("雞:%d 兔:%d" % (chicken, rabbit))
