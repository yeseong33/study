# 사용자로부터 문자열을 받아 문자, 숫자, 공백의 개수를 출력하는 프로그램을
# 작성

space = 0
alphabet = 0
num = 0

s = input('문자열을 입력하세요 : ')
if len(s) > 0:
    for ch in s:
        if ch.isalpha():
            alphabet += 1
        elif ch.isdigit():
            num += 1
        elif ch == ' ':
            space += 1
    print('문자의 개수 : ', alphabet)
    print('숫자의 개수 : ', num)
    print('공백의 개수 : ', space)

