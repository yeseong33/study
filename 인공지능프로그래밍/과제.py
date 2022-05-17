# # 완전수 구하기
# for n in range(1,1001):
#     sum = 0
#     for i in range(n):
#         if n % (i + 1) == 0:
#             x = n // (i + 1)
#             if x > i + 1:
#                 sum += x + (i + 1)
#             elif x == i + 1:
#                 sum += x
#             else:
#                 sum_f = sum - n
#                 if sum_f == n:
#                     print(sum_f,'는 완전수',sep='')
#                 break


# 커피자판기
print('----------------')
int(input('요금을 투입 하세요\n>'))
print('----------------------------------------')
print('========커피자판기========')
print('1. 커피<200>\t2. 코코아<250>\t3. 반환\t4.종료')
input('메뉴를 선택하세요\n>')





