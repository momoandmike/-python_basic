import random

men = input('サイコロの面数は？：')
cnt = input('何回振りますか？：')

dice = []
for result in range(0, int(cnt)):
    dice.append(random.randint(1, int(men)))
print(dice)
