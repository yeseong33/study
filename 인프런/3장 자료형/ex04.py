# 문자열에 대한 실습


# 큰따옴표(double quotation)
welcome = "Happy New Year 2021"
print(welcome)

# 작은따옴표(single quotation)
welcome = 'Happy New Year 2021'
print(welcome)

#문자열을 만들때 시작을 : " 으로 했는데 '으로 끝을 낸다면, EOL(End of Line) 에러가 발생한다.
# 그 이유는 "로 시작을 했는데 "의 끝 내용을 찾을 수 없다라고 하는 것이다.

# welcome = 'Happy New Year 2021"
# print('welcome')

# message = "은혁이가 "안녕하세요"라고 인사했습니다."
# print(message)

# \가 있으면 뒤에 문자는 특수한 의미를 잃어버린다.
message = 'dosen\'t'
print(message)

# 특수문자 형태인 \n은 개행(Enter)을 하는 문자이다.
message = 'Fist\nSecond\nThird'
print(message)

# 특수문자 \t는 탭만큼 띄우는 문자이다.
message = 'c:\temp\name'
print(message)

# 위에서 본 이스케이프문자들의 기능을 제거시키기 위해
# r를 시작앞부분에 붙여준다.
message = r'c:\temp\name'
print(message)

# \는 뒤의 문자의 특수한 의미를 없앤다.
message = 'c:\\temp\\name'
print(message)

# 문자열(영어, 한글 상관없음)의 길이를 알고자 한다면 len()함수를 이용한다.
message = 'world'
print('문자열의 길이 : ',len(message))
