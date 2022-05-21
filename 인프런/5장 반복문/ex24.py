# 입력받은 문자열의 모든 공백을 제거한 문자열을 출력하는 프로그램을
# 작성

s = input('문자열을 입력하세요 : ')
result = ''

for ch in s:
    if not ch.isspace():
        result += ch

print('입력한 문자열 :', s)
print('공백을 제거한 문자열 :', result)