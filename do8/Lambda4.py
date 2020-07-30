if __name__ == '__main__':
    lev = ['E', 'E', 'E', 'E', 'E', 'E', 'D', 'C','B', 'A', 'A' ]

    dict = {
        'level' : lambda score : print(lev[score//10])
    }

dict.get('level')(95)
dict.get('level')(85)
dict.get('level')(75)
dict.get('level')(65)
dict.get('level')(55)
dict.get('level')(25)







