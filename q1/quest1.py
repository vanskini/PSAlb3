filename = 'test1.txt'

line1 = 'Аэрофотосъёмка ландшафта уже выявила земли богачей и процветающих крестьян.\n'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(line1)

line2 = 'Подъехал шофёр на рефрижераторе грузить яйца для обучающихся элитных медиков.\n'
with open(filename, 'a', encoding='utf-8') as f:
    f.write(line2)

with open(filename, encoding='utf-8') as f:
    print(f.read())
