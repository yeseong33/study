# while 문의 실습
# while 문은 조건을 정해놓고 반복을 하는 구조이다.

i = 0
while i < 5:
    print('반갑습니다.')
    i += 1   # 만약 좌측 코드가 없다면 while 문은 무한 루프를 돈다.
print('반복이 종료되었습니다.')


# 숫자 0~9까지 줄바꿈을 하지 아니하고 출력해보기(while 문 사용)
i = 0
while i < 10:
    print(i, end=' ')
    i += 1
print('')
print('----------------')
# 1~10 까지의 누계합을 구하는 예제
i = 1
hap = 0
while i <=10:
    hap += i
    i += 1
print('1~10 까지의 누계합 : ', hap)


# while 문을 사용하여 팩토리얼을 구하는 예제
# f(1) = 1
i = 1
fa = 1

while i <= 10:
    fa *= i
    i += 1
print('10!의 값은 %d 입니다.'% fa)


# while 문을 사용하여 3단을 구하는 예제
i = 1
while i <= 9:
    # % 뒤에 오는 숫자들은 출력할 때 자릿수를 차지하게끔 만들어준다.
    # %.1f %0.1f 는 동일한 자리값을 출력한다. (소수점 첫째까지)
    print('3 * %d = %2d' % (i, 3*i))
    i += 1


# 1~100 까지의 3의 배수만 누적값을 구하는 예제
hap = 0
i = 1
while i < 100:
    if i % 3 == 0:
        hap += i
    i += 1
print('1~100 까지의 모든 3의 배수의 합은 %d 입니다.' % hap)
print('---------------------------')


# 정수 안의 각 자리수의 합을 계산하는 예제
# 예를 들어 1234라면 (1+2+3+4)를 계산
num = 1234
hap = 0
i = 0
while len(str(num)) > i:
    hap += int(str(num)[i])
    i += 1
print(hap)

num = 1234
hap = 0
while num > 0:
    digit = num % 10  # 해당하는 자릿수의 값을 구하는 코드
    hap += digit
    num = num // 10 # 10 으로 나누어 줌으로써 몫만 num에 저장되는 코드
print('1234 정수의 자리수의 합은 %d 입니다.' % hap)

