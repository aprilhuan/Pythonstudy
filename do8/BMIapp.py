import do8.BubbleSort3 as bb

rows = [{'h':170, 'w':60},
        {'h':160, 'w':55},
        {'h':180, 'w':70}]


for row in row:
        w = row.get('w')
        h = row.get('h')
        bmiValue = w/(h/100)**2
        row.setdefault('bmi', bmiValue)

rows = bb.sort('bmi', rows)
print(rows)

