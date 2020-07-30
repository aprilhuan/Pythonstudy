def sort(rows, flag=True):
    for i in range(0, len(rows)):
        for j in range(i + 1, len(rows)):
            x = rows[i]
            if flag:
                if rows[i] > rows[j]:
                   rows[i] = rows[j]
                   rows[j] = x
            else:
                if not

if __name__ == '__main__' :
    rows = [
            {"age":10, "score":90},
            {"age":40, "score":100},
            {"age":20, "score":80}
           ]
#rows = bb.sort('h', rows)
#rows = bb.sort('w', rows)


rows = sort('score', rows)
print(rows)



