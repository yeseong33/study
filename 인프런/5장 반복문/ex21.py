# 반복문으로 문자열 관련 처리하기
fruit = 'apple'
# fruit 문자열 변수에 값을 하나씩 문자 형태로 가져와 출력하는 코드
for letter in fruit:
    print(letter, end = ' ')
print('')
print('------------------------')

# 사용자로부터 문자열(영문)을 입력받아서 모음을 전부 없애는 코드
s = input('문자열을 입력하세요(영문자) : ')
# 영문자의 모음의 문자열
vowels = 'aeiouAEIOU'
result = ''
for letter in s:
    if letter not in vowels:
        result += letter
print('자음만 출력 :', result)

# 문자열을 입력받아서 자음과 모음의 개수를 집계하는 코드
original = input('문자열을 입력하세요 : ')
# 입력받은 문자열을 소문자로 변경
word = original.lower()
vowels = 0
consonanats = 0

if len(original) > 0 and original.isalpha():
    for ch in word:
        if ch in 'aeiou':
            vowels += 1
        else:
            consonanats += 1

    print('모음의 개수 :', vowels)
    print('자음의 개수 :', consonanats)
