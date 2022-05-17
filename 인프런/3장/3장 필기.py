# 3장 필기

# 파이썬의 자료형
# 1. 정수(integer): 1,2,3,4,5
# 2. 실수(float-point): 1.1, 1.4
# 3. 문자열(string): 'hi', '123'

# 1) 파이썬의 문자열
# 문자열 안에서 구별하기 위해 '' 와 "" 가 존재한다.
#
# print('고로고\'록로 ')

# \n 은 줄바꿈을 해서 출력해준다.
# \t 은 tap을 표현한다.
#
# print('c:\temp\name')
# print(r'c:\temp\name')
# r를 문자열 앞에 붙여 특수문자를 취급하지 않는다.
#
# 2) 문자열의 연결
# 파이썬 쉘에서 2개 이상의 문자열이 서로 붙어 있으면 자동으로 연결된다.
#
# 'Py''thon'
# + 연산자로도 합칠 수 있다.
#
# 3) 문자열과 정수간의 변화
#
#
# 4) 문자열의 반복
# line = '=' * 50
# print(line)
#
# 5) 문자열의 출력
# 문자열에 변수의 값을 삽입해 출력하고 싶으면 %s를 사용한다.
#
# price = 10000
# print('상품의 가격은 %s원입니다.'%price)
#
# massage = '현재시간은 %s입니다.'
# time = '12:00am'
# print(massage%time)

# 6)인덱싱
# 인덱싱(Indexing)이란 문자열이 []에서 문자를 추출하는 것이다.
# 인덱스는 문자열에 포함된 각각의 문자에 매겨진 번호이다.
# 0,1,2,3,4,5
# -6,-5,-4,-3,-2,-1 # 음수 인덱스도 존재한다.

