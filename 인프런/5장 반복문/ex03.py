# 1부터 사용자가 입력한 수 num 까지 더해서 합계를 구하는 프로그램을
# for 문을 이용해 작성하시오.

hap = 0
num = int(input('수를 입력하세요: '))
for i in range(1, num+1):
    hap += i
print(hap)
