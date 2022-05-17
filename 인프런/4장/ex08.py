# 사용자로부터 두 개의 정수를 입력받아서 둘 중에서 큰 수를 출력하는 프로그램
# 만들기

# x = int(input('첫번째 정수를 입력하세요 : '))
# y = int(input('두번째 정수를 입력하세요 : '))
#
# if x > y:
#     print(x,'가',y,'보다 큼니다.')
# else:
#     print(y,'가',x,'보다 큼니다.')


x = int(input('첫번째 정수를 입력하세요 : '))
y = int(input('두번째 정수를 입력하세요 : '))
maximum = 0
if x > y:
    maximum = x
else:
    maximum = x
print('둘 중에 큰 수 : ', maximum)
