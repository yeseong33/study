# 입력받은 문자열을 거꾸로 출력하는 프로그램

s = input('문자열을 입력하세요 : ')
s_reverse = ''
# for 문을 활용한 방법
for ch in s:
    s_reverse = ch + s_reverse

print('입력한 문자열 : ' + s)
print('역순으로 출력한 문자열 : '+ s_reverse)

# 리스트를 활용한 방법
# 리스트 뒤집기, 문자열 뒤집기
s_list = list(s)
print(s[::-1])

# reversed() 는 문자열을 역순으로 해준다.
print(''.join(reversed(s)))
