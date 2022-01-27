list = input("データを入力してください > ")


# 合計値

def total():
    if len(list) < 1:
        return len(list)
    return len(list) + total(len(list) - 1)

# 最大値
# 最小値
# 平均値


# 再帰関数を使う？
