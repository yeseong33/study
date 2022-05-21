s = '      안녕  !     '

# 왼쪽 공백만 제거하는 함수 ( lstrip)
print('제거 전 문자열 :' + s)
print('왼쪽 공백 제거 :' + s.lstrip())

# 오른쪽 공백만 제거하는 함수 ( rstrip)
print('제거 전 문자열 :' + s)
print('왼쪽 공백 제거 :' + s.rstrip())

# 양쪽 공백 제거하는 함수 ( strip)
print('제거 전 문자열 :' + s)
print('양쪽 공백 제거 :' + s.strip())


# 문자열 나누기, 문자열을 리스트로 나눌 수 있다.
s = '나는 배가 많이 코파요..'
print(s.split())
