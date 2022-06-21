money = 100
heads = 0
bull = 10
cow = 5
calf = 0.5
bull_counter = 0
cow_counter = 0
calf_ccounter = 0

for b in range(1, 11):
    for ca in range(1, 100):
        for c in range(1, 21):
            if b * 10 + c * 5 + ca * 0.5 == 100 and b + ca + c == 100:
                print(b, c, ca)
