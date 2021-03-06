# 자동 판매기를 시뮬레이션하는 프로그램은 작성하는데, 사용자는 1000원짜리 지폐와
# 500원, 100원짜리 동전을 사용할 수가 있다. 물건값을 사용자로부터 입력을 받아서
# 1000권 지폐, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 거스름돈을 계산해서
# 동전으로 반환하는 프로그램을 만들어보자.

## 내 코드
# price = 5000
# money = int(input('돈을 입력하세요.: '))
# ex = price - money
# c1000 = ex // 1000
# c500 = (ex % 1000) // 500
# c100 = ((ex % 1000) % 500)/100
# print('c1000:',c1000)
# print('c500:',c500)
# print('c100:',int(c100))


# 풀이
itPrice = int(input('물건값을 입력하세요 : '))
bills_1000 = int(input('1000원 지폐 개수 입력 : '))
coin_500 = int(input('500원 동전 개수 입력 : '))
coin_100 = int(input('100원 동전 개수 입력 : '))

# 거스름돈 구하기
nod_money = (bills_1000 * 1000) + (coin_500 * 500) + (coin_100 * 100) - itPrice
print('거스름돈 : ',nod_money)
# 거스름돈(500원 동전 개수)를 계산
nCoin500 = nod_money // 500
nod_money = nod_money % 500  # 500원으로 나눈 나머지 값

# 거스름돈(100원 동전 개수)를 계산
nCoin100 = nod_money // 100
nod_money = nod_money % 100  # 100원으로 나눈 나머지 값

# 거스름돈(50원 동전 개수)를 계산
nCoin50 = nod_money // 50
nod_money = nod_money % 50  # 50원으로 나눈 나머지 값

# 거스름돈(10원 동전 개수)를 계산
nCoin10 = nod_money // 10
nod_money = nod_money % 10  # 10원으로 나눈 나머지 값

# 거스름돈(100원 동전 개수)를 계산
nCoin1 = nod_money

print('500원 개수 : ', nCoin500,' 100원 개수 : ',nCoin100, ' 50원 개수 : ',nCoin50,
      ' 10원 개수 : ', nCoin10,' 1원 개수 : ',nCoin1)

print(4500+200+50+10+5)