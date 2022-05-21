# 학점을 세부적으로 나누는 프로그램을 작성하기(중첩 if 문 사용)
# 조건
# 1. 사용자로부터 점수를 입력받는다.
# 2. 점수가 95 이상 100 이하라면 A+ 을 출력
# 3. 점수가 90 이상 94 이하라면 A0을 출력한다.
# 단, F는 그냥 출력하자.

G = int(input('점수를 입력하세요 : '))
print('입력한 점수 : ', G)

if G >= 90:
    if G >= 95:
        print('학점은 A+ 입니다.')
    else:
        print('학점은 A0 입니다.')
elif G >= 80:
    if G >= 85:
        print('학점은 B+ 입니다.')
    else:
        print('학점은 B0 입니다.')
elif G >= 70:
    if G >= 75:
        print('학점은 C+ 입니다.')
    else:
        print('학점은 C0 입니다.')
elif G >= 60:
    if G >= 65:
        print('D+ 입니다.')
    else:
        print('D0 입니다.')
else:
    print('F 입니다.')