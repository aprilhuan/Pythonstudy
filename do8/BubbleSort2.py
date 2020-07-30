rows = [
    {"age":10, "score":90},
    {"age":40, "score":90},
    {"age":20, "score":90}
    ]

for i in range(0, len(rows)):
    for j in range(i+1, len(rows)):
        x = rows[i]
        if rows[i].get('score') > rows[j].get('score'): # 排序欄位比較
            rows[i] = rows[j]
            rows[j] = x

if __name__ == '__main__' :
    rows = [
             {"age":10, "score":90},
            {"age":40, "score":100},
            {"age":20, "score":80}
           ]

    rows = sort ('score', rows)
    print(rows)