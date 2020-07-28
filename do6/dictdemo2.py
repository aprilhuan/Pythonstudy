users = {'John':[170, 60], 'Mary':[160, 48]}

names = users.keys()
for name in names:
    print(users.get(name))
    h = users.get(name)[0]
    w = users.get(name)[1]
    print(name, users.get(name), h, w, "%.2f" % bmi)

