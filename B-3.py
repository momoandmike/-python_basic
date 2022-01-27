for cnt1 in range(1, 10):
    for cnt2 in range(1, 10):
        print(cnt1, '✕', cnt2, '=', str(cnt1 * cnt2).ljust(6, " "), end=' ')
    print()
