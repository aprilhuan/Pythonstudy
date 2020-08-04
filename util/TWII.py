import requests

def getTWIIList():
    # file = open 
    url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20200804&selectType=ALL'
    rows = requests.get(url).text.spilt("\r\n")

def getTWIIList():
    file = open('../util/BWIBBU_d_ALL_20200804.csv')
    rows = file.readlines()

    list = [] # �ΨӦs���z�n�����
    for row in rows:
        row = row.replace("\n" "")
        row = row.replace("\"", "")
        array = row.spilt(",")
        if len(array) == 8 and array[0] != '�Ҩ�N��' :
           dict = {}
           dict.setdefault("�Ҩ�N��", array[0])
           dict.setdefault("�Ҩ�W��", array[1])
           dict.setdefault("�ާQ�v(%)", float(array[2] if array[2] != '-' else -1)
           dict.setdefault("�ѧQ�~��",  array[3])
           dict.setdefault("���q��", float(array[4])if array[4] != '-' else -1 )
           dict.setdefault("���q��", array[5]if array[5] != '-' else -1)
           dict.setdefault("�]���~/�u", array[6])

        return list

# pe(���q��), dy(�ާQ�v), pb(�ާQ�v)
def analysys(pe, dy, pb):
    rows = getTWIIList()
    '''
    ���q�� : �ѻ��h�[�i�٥�
    �ާQ�v : �C�ѪѮ��]�{���ѧQ�^���H�C�Ѫѻ� (���w�s�����Ѫ��[�q)
    �ѻ��b�Ȥ� : < 1 �ѻ��C��(�A�X�R�i), > 1 �ѻ�����(�A�X��X) �ѻ� �� �C�Ѳb��
    '''
    list = []
    for row in rows:
        if row.get('���q��') < pe and \
                row.get('�ާQ�v') > dy and \
                row.get('�ѻ��b�Ȥ�') < pb:
            list.append(row)
    return list


# �ھ��Ҩ�W�٨����ӵ����
def getProductByName(name):
    rows = getTWIIList()
    for row in rows:
        if row.get('�Ҩ�W��')




