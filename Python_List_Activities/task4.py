months_avg_temp = [
    ["January", 10, -15],
    ["February", 6, -20],
    ["March", 18, 2],
    ["April", 20, 12],
    ["May", 31, 14],
    ["June", 33, 20],
    ["July", 34, 21],
    ["August", 31, 24],
    ["September", 26, 19],
    ["October", 19, 10],
    ["November", 13, 0],
    ["December", 12, -10]
]

hottest = -273
hottest_month = ""
coldest = 100
coldest_month = ""

for month in months_avg_temp:
    if month[1] > hottest:
        hottest = month[1]
        hottest_month = month[0]
    if month[2] < coldest:
        coldest = month[2]
        coldest_month = month[0]

print(f"Hottest month: {hottest_month}, average temperature: {hottest}")
print(f"Coldest month: {coldest_month}, average temperature: {coldest}")
