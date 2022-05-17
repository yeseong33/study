# 몸무게와 키를 입력받고 BMI가 20.0이상이고 25미만이면
# 표준입니다 라고 출력을 하고 아니면 체중관리가 필요합니다 라고
# 출력하는 프로그램

# BMI = 몸무게 / (키 * 키)
# 키를 m로 환산해야 한다.

# 내 코드
weight = float(input('몸무게를 입력하세요 : '))
height = float(input('키를 입력하세요 : '))
BMI = weight / (height/100) ** 2
print('BMI 값 : ', BMI)

if 20.0 <= BMI < 25.0:
    print('몸무게가 표준입니다.')
else:
    print('체중관리가 필요합니다.')

# 풀이
height = float(input('키(cm)를 입력 : '))
weight = float(input('몸무게(kg)를 입력 : '))
height /= 100
BMI = weight / height ** 2
print('BMI 값 : ', BMI)

if BMI >= 20.0 and BMI <= 25.0:
    print('표준입니다.')
else:
    print('체중관리가 필요합니다.')



