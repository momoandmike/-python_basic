for cnt1 in range(1, 10):
    for cnt2 in range(1, 10):
        print(cnt1, '✕', cnt2, '=', cnt1 * cnt2, end="".ljust(6, " "))
    print()

# 途中からずれてしまう。
