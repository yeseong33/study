# 사용자의 전화번호를 입력받는다.
# '-'을 포함해 입력받고 출력시 삭제한 뒤 출력하는 프로그램 작성

num = input('전화번호를 -를 포함해 입력 : ')
result = ''

for ch in num:
    if ch.isdigit():
        result += ch
print(result)