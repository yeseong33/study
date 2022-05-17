# 사용자로부터 2개의 정수 값을 입력받고 첫 번째 입력받은 값부터 두 번째 입력
# 받은 값까지의 범위에서 3의 배수이면서 4의 배수인 수를 제외하고 출력하는
# 프로그램을 작성하시오.

n1 = int(input('시작 정수를 입력하세요. : '))
n2 = int(input('끝 정수를 입력하세요. : '))

for i in range(n1, n2+1):
    if i % 3 != 0 or i % 4 != 0:
        print(i, end=' ')


for i in range(n1, n2+1):
    # continue 는 조건식이 차밍면 아래 문장을 실행시킨다.
    if i % 3 == 0 and i % 4 == 0:
        continue
    print(i, end=' ')