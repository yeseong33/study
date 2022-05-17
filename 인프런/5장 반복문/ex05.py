# for 문을 이용해 펙토리얼을 계산하는 프로그램을 작성해보자
# 팩토일얼 n! 은 1부터 n 까지의 정수를 모두 곱한 것을 의미하는 것이다.

n = int(input('n을 입력하세요 : '))
k = 1
for i in range(1, n+1):
    k *= i
    
print(k)
