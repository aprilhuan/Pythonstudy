class Account:
    __money = money = 0 # �����ݩ� �ܼ� �겣

    def __init__(self, x): -> None:  # �غc��
        self.__money = x # �}��ɩҦs���Ĥ@�����B

    def transfer(self, account name, x):
        print("��b��" + accountName + " ���B: $" + str(x))
        if x <= 0:
            print('��b���B >�@��')
            return

    def save(self, x):
        print("�s��: $" + str(x))
        if x<= 0:
            print('���ڪ��B���� > 0')

    def withdraw(self, x): # x ��ܭn���ڪ����B
        print("����: $ ") + str(x))
        if x <= 0:
            print('���ڪ��B���� > 0')
            return
        if x > self.__money:
            print('���ڪ��B�L�j, �l�B���w')
            return
        self.money = self.__money - x



    def __str__(self) -> str:
        return "�b��l�B:" + str(self.money)

if __name__ == '__main__':
    account1 = Account() # �إߤ@����
    print(account1)
    account1.withdraw(6000)
    print(account1)
    account1.withdraw(-6000)
    print(account1)
    account1.save(5000)
    print(account1)

