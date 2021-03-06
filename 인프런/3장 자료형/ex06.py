# 문자열의 인덱싱
# 인덱싱이란 문자열에서 문자를 추출하는데 문자열에는 각각에 해당하는 문자에 번호(인덱스)가
# 존재한다. [인덱스] 하면 문자열에서 문자를 추출할 수가 있다.
# 인덱스라 함은 0부터 시작한다. 마지막 인덱스는 n-1이 성립된다.
# 파이썬의 특수기능인 인덱스를 처리할 때 음수도 사용이 가능하다.


word = 'Python'
print(len(word))

print(word[0])
print(word[5])
print(word[-1])
#
print(word[len(word)-1])

# 해당 문자열의 인덱스의 범위 밖에 값을 주면 index out of range 라는 에러가 발생한다.
# print(word[100])

# 파이썬에서는 한번 작성된 문자열은 변경이 불가능하다.(다른언어에서는 가능)
# word[2] = 'B'

# 사용자로부터 문자열을 입력을 3개을 받도록 한다. 해당 문자열의 첫 번째 문자를 인덱싱하여
# 문자를 합쳐서 문자열로 만드는 프로그램을 만들어 보자.

word1 = input('첫번쩨 문자열을 입력하세요 : ')
word2 = input('두번쩨 문자열을 입력하세요 : ')
word3 = input('세번쩨 문자열을 입력하세요 : ')
# 위의 3개의 문자열 중 첫 번째 단어만 추출해 또다른 문자열을 만들고 있다.
mixWord = word1[0]+word3[0]+word3[0]
print(mixWord)

