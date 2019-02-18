reshta = int(input('Введіть решту '))
vuvid = reshta
quater = 25
dime = 10
nickel = 5
penny = 1
count = 0
while reshta != 0:
    if reshta >=25:
        reshta = reshta - quater
        count = count + 1
    if reshta >= 10 < 25:
        reshta = reshta - dime
        count = count + 1
    if reshta >= 5 < 10:
        reshta = reshta - nickel
        count = count + 1
    if reshta >= 1 < 5:
        reshta = reshta - penny
        count = count + 1
print('O hai!How much change is owned')
print(f'0.{vuvid}')
print(count)

