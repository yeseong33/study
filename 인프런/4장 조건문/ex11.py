# 문자열의 중앙에 있는 문자를 추출해 출력하는 프로그램을 만들기
# 예를 들어 문자열이 'weekday'라면 중앙의 문자는 'k'가 된다.
# 만약 문자열이 짝수개의 문자를 가지고 있다면 중앙에 문자 2개를
# 출력한다.

# 내 코드
string = input('문자열을 입력하세요. : ')

if len(string) % 2 == 0:
    len_1 = len(string) // 2
    a = len_1 - 1
    b = len_1 + 1
    c = string[a:b]
    print(c)
else:
    len_1 = len(string) // 2
    c = string[len_1]
    print(c)

# 풀이
# str_1 = input('문자열을 입력하세요 : ')
# length = len(str_1)
#
# if length % 2 == 1:
#     ch = str_1[length//2]
#     print('중앙에 있는 한 글자는 ', ch)
# else:
#     ch1 = str_1[length//2 - 1]
#     ch2 = str_1[length // 2]
#     print('중앙에 있는 두 글자는 ', ch1, ch2)
