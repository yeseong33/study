# 사용자로부터 상품금액을 입력받아서 상품의 총 가격을 계산하는 프로그램 만들기
# 사용자가 몇 개의 상품을 살지 모르니 무한루프를 이용하고 아울러 사용자가
# 끝 이라고 입력하면 루프를 탈출하게끔 조건을 주도록 한다.

total = 0
price = 0

while price != '끝':
    total += int(price)
    price = input('상품의 가격을 입력하세요 : ')
print('총 가격은', total, '입니다.')


from operator import eq


total = 0
price = ''
while True:
    price = input('상품 금액을 입력하세요.(끝을 입력하면 종료됨) : ')
    if eq(price, '끝'):     # if price == '끝' 과 동일한 코드
        print('총 가격은', total, '원 입니다.')
        break
    total += int(price)


