def hotdog(func):
    print("我是熱狗")
    return func


@hotdog
def bread(func):
    print("我是麵包")
    return func


if __name__ == '__main__':
   bread()