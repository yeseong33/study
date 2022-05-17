# 사용자로부터 태어난 연도를 입력받아서 초, 중, 고, 대 학생을 분류해보세요
# 단, 나이 : 8 ~ 13 초등, 14 ~ 16 중학생, 17 ~ 19 고등학생, 20 ~ 27 대학생 이 외에
# 나이라면 일반인으로 분류를 하도록 한다.

year = int(input('태어난 연도를 입력하세요 : '))
age = 2022 - year + 1
print('현재 나이 : ', age)

if 8 <= age <= 13:
    print('초등학생입니다.')
elif 14 <= age <= 16:
    print('중학생입니다.')
elif 17 <= age <= 19:
    print('고등학생입니다.')
elif 20 <= age <= 27:
    print('대학생입니다.')
else:
    print('일반인입니다.')