gyo = input('行数を入力してください:')
rtu = input('列数を入力してください:')

for cnt1 in range(1, int(gyo) + 1):
    for cnt2 in range(1, int(rtu) + 1):
        print(int(cnt1) * int(cnt2), end="")
    print()
