# 사용자로부터 달을 입력받아서 입력한 달의 일수를 구하는 프로그램을 작성하기

month = int(input('월을 입력하세요 : '))
day = 0
if 1<= month <12 and month % 2 == 0:
    if month == 2:
        day = 28
    else:
        day = 30
elif month > 12:
    print('1~12 사이의 정수를 입력해주세요')
else:
    day = 31

print('입력한 ',month,'월의 일수는 ',day,'일 입니다.',sep = '')

