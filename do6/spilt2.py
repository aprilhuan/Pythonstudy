data = '170,60&160,48'
# 試算出這二筆 bmi 值各是多少 ?

for row in data.split("&"):
    print(row, type(row))
    for r in row.split(","):
        print('\t', r, type(r))
        bmi = "%.2f" % (float(r[1])/(float(r[0])/100)**2)
        print(bmi)
