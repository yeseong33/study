# 반복문

# 반복문의 필요성
# 동일한 명령어를 여러번 실행해야 하는 경우

# for 문: 정해진 횟수만큼 반복하는 구조(더 많이 쓰임)
# while 문: 어떤 조건이 만족되는 동안 반복을 계속하는 구조(무한 루프용으로 쓰임)


# for 문
# 정해진 횟수만큼 반복할 때 사용하는 구조
# 반복 구조중 가장 많이 사용된다.(장점이 많음)

# for 변수 in 시퀀스
# 시퀀스: 문자열이나 리스트

#  range 의 메모리 낭비를 줄이기 위해 제네레이터라는 객체를 이용한다.


# while 문
# 조건을 정해 놓고 반복을 하는 구조
# 조건이 참이면 반복, 거짓이면 반복루프를 빠져나간다.

# while 조건:
#   내용

# 무한루프가 나오지 않게 프로그램을 작성해야 한다.
# 무한루프를 프로그램으로 작성하면 어떤조건일 때 루프를 빠져나가는지 반드시
# 기술한다.

# 보초값(sentinel) 사용하기
# 데이터가 많아 개수를 알기 힘든 경우에 사용
# 데이터의 끝에 끝을 알리는 특수한 데이터를 추가한다.
# 이러한 데이터 값을 보초값이라 한다.
# 예를 들어 성적을 입력 받는 프로그램의 경우 음수나 100을 초과하는 값을 보초값으로
# 설정한다.


# 중첩루프
# 반복문은 증첩해서 사용될 수 있다. 이를 중첩반복문(nested loop)이라 하고, 외부의 반복문을
# 외부 반복문(outer loop)라고 하며, 안쪽의 반복문을 내부 반복문(inner loop)라고 한다.
# 내부반복문은 외부 반복문이 한번 반복할 때마다 다시 실행 된다.

# ex
# for y in range(5):
#     for x in range(10):
#         print('*', end = '')
#     print('')

# 반복문으로 문자열 처리
# 문자열을 처리하는 용도로 반복문이 많이 사용됨
# fuit = 'apple'
# for letter in fuit:
#     print(letter, end ='')

# 문자열을 받아서 모음을 없애는 코드
# s = input('문자열을 입력하세요')
# vowels = 'aeioAEIOU'
# result = ''
# for letter in s:
#     if letter not in vowels:
#         result += letter
# print(result)

# ex
# 문자열 중에서 자음과 모음의 개수를 집계하는 프로그램
original = input('문자열을 입력하세요 : ')
word = original.lower()
vowels = 0
consonants = 0

if len(original) > 0 and original.isalpha():
    for char in word:
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print('모음의 개수 :', vowels)
print('자음의 개수 :', consonants)