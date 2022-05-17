# 문자열의 연결
# +연산자는 문자열 사이에 들어가면 문자열을 연결해주는 역할을 한다.
first_name = 'Yeeong'
last_name = 'Oh'
name = last_name + first_name
print(name)

# 파이썬에서는 모든 데이터에는 데이터 타입이 존재한다. 아래 소스코드에서 확인을 하면
# 'Person'은 문자열이고, 100은 int 타입이다. 하여 타입의 일치가 되지 않아 서로
# 연결을 하는데 에러가 발생한다.
# temp = 'Person' + 100
# print(temp)

temp = 'Persom' + str(100.213) + str(100)
print(temp)

# 문자열을 숫자로 변환
# 정수일 때
price = int('12345')
print(type(price))
print(price )
# 실수일 때
price = float('12345.132123')
print(type(price))
print(price )

# 문자열의 반복
arrow = '->' * 10
print(arrow)

print(arrow *  100)

# %s(형식 지정자)
# %s는 문자열이나 숫자를 변수에 대입해 자주 변경이 있을 겨우 이런 형식을 지정해
# 상황에 맞게끔 출력을 하도록 하면 될 것이다.

# %s에 정수를 대입
price = 1000
print('가격 : %s' % price)

# %s에 문자열을 대입
time = '13.49'
print('현재시간 : %s' % time)

temp = '현재 시간은 %s시 %s분 %s 초입니다. '
print(temp % (10,38,12))

