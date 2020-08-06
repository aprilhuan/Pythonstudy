import os
import atm.Account as act
# �D�{��
act1 = act.Account(1000)
act2 = act.Account(1000)
act3 = act.Account(1000)
list = [{"john: act1"}, {"mary: act2"}, {"tom: act3"}]

def display():
    for act in list:
        for key in act.keys():
            print(key, act.get(key))
def save():
    actName = input('�п�J�s�ڪ��B')
    x = int(input('�п�J�s�ڪ��B'))
    # �o��s�ڤH��account����
    account = None
    for act in list:
        for key in act.keys():
            if key == actName:
                account = act.get(key)
    if account == None:
        print('�d�L���H')
    else:
        account.save(x)

def withdraw():
    actName = input('�п�J���ڤH: ')
    x = int(input('�п�J���ڪ��B: '))
    # �o�촣�ڤH��account����
    account = None
    for act in list:
        for key in act.keys():
            if key == actName:
                account = act.get(key)
    if account == None:
        print('�d�L���H')
    else:
        account.withdraw(x)

def transfer():
    fromName = input('�п�J��b�H(from): ')
    toName = input('�п�J�Q��b�H(to): ')
    x = int(input('�п�J��b���B: '))
    fromAccount = None
    toAccount = None
    for act in list:
        for key in act.keys():
            if key == fromName:
                fromAccount = act.get(key)
            if key == toName:
                toAccount = act.get(key)
    if fromAccount == None or toAccount == None:
        print('�d�L���H')
    else:
        fromAccount.transfer(x, toAccount)


def createAccount():
    accountName = input('�п�J�}��H�W��:')
    x = int(input('�п�J�}����B: $'))
    account = act.Account(x)
    dict = {accountName: account}
    list.append(dict)


def cancelAccount():
    cancelName = input('�п�J�Ѭ��H:')
    cancelAccount == None:
    for act in list.keys():
        if key in act.keys():
            if key == cancelName:
                cancelAccount = act.get




# �t�ο��
while True:
    print('�t�ο��:')
    print('-----------')
    print('1. �d�� ')
    print('2. �s��' )
    print('3. ����')
    print('4. ��b')
    print('5. �}��')
    print('9. ���}')
    print('-----------')
    no = int(input('�п��(1~9): '))
    if no == 1:
        display()
    elif no == 2:
        save()
    elif no == 3:
        withdraw()
    elif no == 4:
        transfer()
    elif no == 5:
        createAccount()
    elif no == 9:
        break
    os.system('pause') # �Ȱ�(�U���@����~��)

print('�{������')












