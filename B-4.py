weather_information = [
    {'prefecture': '東京都', 'station': '渋谷', 'temperature': 6.5},
    {'prefecture': '東京都', 'station': '池袋', 'temperature': 7.0},
    {'prefecture': '東京都', 'station': '新橋', 'temperature': 7.5},

    {'prefecture': '大阪府', 'station': '梅田', 'temperature': 8.2},
    {'prefecture': '大阪府', 'station': '大阪', 'temperature': 9.3},
    {'prefecture': '大阪府', 'station': '堺', 'temperature': 9.5},

    {'prefecture': '福岡県', 'station': '博多', 'temperature': 13.0},
    {'prefecture': '福岡県', 'station': '太宰府', 'temperature': 15.0},
]

# Q1. 全国の平均気温を計算してください(9.5となればOK)
kion1 = (weather_information[0]['temperature'])
kion2 = (weather_information[1]['temperature'])
kion3 = (weather_information[2]['temperature'])
kion4 = (weather_information[3]['temperature'])
kion5 = (weather_information[4]['temperature'])
kion6 = (weather_information[5]['temperature'])
kion7 = (weather_information[6]['temperature'])
kion8 = (weather_information[7]['temperature'])
sum_kion = kion1 + kion2 + kion3 + kion4 + kion5 + kion6 + kion7 + kion8
avg_kion = sum_kion / len(weather_information)
print(avg_kion)

# Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
osaka1 = weather_information[3]['station']
osaka2 = weather_information[4]['station']
osaka3 = weather_information[5]['station']
print("'" + osaka1 + "," + osaka2 + "," + osaka3 + "'")

# Q3. 福岡県の平均気温を計算してください(14.0となればOK)
fukuoka_kion1 = weather_information[6]['temperature']
fukuoka_kion2 = weather_information[7]['temperature']
sum_fukuoka_kion = fukuoka_kion1 + fukuoka_kion2
avg_fukuoka_kion = sum_fukuoka_kion / 2
print(avg_fukuoka_kion)
