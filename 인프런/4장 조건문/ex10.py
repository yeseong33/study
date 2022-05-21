# 쇼핑몰에서 물건을 구매할 때, 구입액이 5만원 이상이면 5%의 할인을
# 해준다고 하자, 사용자에게 구입 금액을 입력받고 최종적으로 할인 금액
# 과 지불 금액을 출력하는 프로그램 만들기

# 내 코드
# money = int(input('구입액을 입력하세요 : '))
#
# if money > 50000:
#     money = 50000 * 0.95
# print('지불금액은 ', money, '원입니다.', sep='')


# 풀이
total_price = int(input('구입 금액을 입력하세요 : '))

if total_price >= 50000:
    discount = total_price * 0.05
    sales_price = total_price - discount
    print('구입 금액 : ', total_price)
    print('할인 금액 : ', discount)
    print('최종 구입 금액 : ', sales_price)

else:
    print('할인 금액 대상이 되질 않습니다.', total_price, '원을 지불해 주세요.')

