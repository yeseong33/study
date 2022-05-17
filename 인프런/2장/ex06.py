# 정수를 입력받아서 시, 분, 초로 변경하는 프로그램

# MS
# time = int(input('정수를 입력하세요 : '))
# h = time // (60*60)
# m = (time // 60)%60
# s = time % 60
# print('현재 시각은',h,'시',m,'분',s,'초입니다.')

time  = int(input('초를 입력하세요 : '))
second = time % 60
minute = (time //60) % 60
hour = (time // 60) // 60
print('시간 : ',hour)
print('분 : ',minute)
print('초 : ',second)