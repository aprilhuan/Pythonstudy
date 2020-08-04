def bread(func):
    print("我是麵包")
    return func

def hotdog():
    print("我是熱狗")

def egg():
    print("我是雞蛋")

def ham():
    print("我是火腿")

if __name__ == '__main__':
    b1 = bread(hotdog)
    b1()
    b2 = bread(ham(egg))
    b2()