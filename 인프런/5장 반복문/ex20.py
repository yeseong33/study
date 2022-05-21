# 소수를 2부터 계속 더할 때, 2000까지의 합을 구하고
# 마지막으로 더해지는 소수를 출력하는 프로그램을 작성해 보자
# 더블루프, 조건식 사용

total = 0
k = 0

for i in range(2, 2000):
    for j in range(2, i+1):
        if i % j == 0:
            break
    if i == j:
        k = i
        total += k
        print(k)
        print(total)

start_num = 0
num = 0
hap = 0
lastData = 0

for num in range(2, 2000):
    for start_num in range(2, num+1):
        if num % start_num == 0:
            break
    if num == start_num:
        print('소수 : ', start_num)
        hap += start_num
        print('합계 : ', hap)
        lastData = start_num
        print('마지막 소수의 값 : ', lastData)
        print('-------------------------------')