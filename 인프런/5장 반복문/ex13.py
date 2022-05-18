# 사용자로부터 임의의 개수의 성적을 입력받아서 합계와 평균을 계산한 후
# 출력하는 프로그램을 작성해보시오. 단, 센티널은 음수의 값을 사용하시오.
n = 1
hap = 0
i = 0
print('종료하시려면 음수를 입력하세요')
while n > 0:
    n = int(input('성적을 입력하세요 : '))
    if n > 0:
        hap += n
        i += 1
avg = round(hap / i)
print('성적의 합계는 %d 이고, 평균은 %d 입니다.' %(hap, avg))


# 센티널을 사용자에게 제시하는 코드
count = 0
hap = 0
score = 0
avg =0.0
print('종료하시려면 음수를 입력하세요')
while score >= 0:
    score = int(input(str(count+1) + '번째 학생의 성적을 입력하주세요 :'))
    # 음수값인지 검사하는 코드
    if score >= 0:
        hap += score
        count += 1
if count > 0:
    avg = hap / count
print(str(count)+'명의 학생의 평균은 %0.1f입니다.' % avg)