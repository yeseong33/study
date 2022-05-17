# 사용자로부터 정수를 입력받아서 음수, 0, 양수 중에 어떤 값인지를 출력하는 프로그램

num = int(input('정수를 입력하세요 : '))

if num > 0:
    print(num,'은 양수입니다.')
elif num < 0:
    print(num,'은 음수입니다.')
else:
    print(num,'은 0입니다.')