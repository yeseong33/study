# 대학을 졸업하려면 적어도 140학점을 이수해야 하고 평점은 2.0은 되어야 한다고
# 하자. 이것을 프로그램으로 만들어 보자
# 사용자에게 이수학점과 평점을 입력받아 졸업가능 여부를 확인하는 것을 코드로
# 작성해보자

# 내 코드
P = int(input('이수학점을 입력하세요. : '))
G = float(input('평점을 입력하세요. : '))

if P >= 140 and G >= 2.0:
    print('졸업이 가능합니다.')
else:
    print('졸업이 불가능합니다.')

# 풀이
hakjum = float(input('이수한 학점을 입력하세요 : '))
grade = float(input('평점을 입력하세요. : '))

if hakjum >= 140 and grade >=2.0:
    print('졸업이 가능합니다.')
else:
    print('졸업이 불가능합니다. 남은 학점을 이수하시길 바랍니다.')