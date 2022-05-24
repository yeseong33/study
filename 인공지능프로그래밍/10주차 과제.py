# # # 짝짓기
def findMatch(l1, l2):
    k = []
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            k.append([l1[i]] + [l2[i]])
    return k


for i in range(3):
    a = input('목록1:').split()
    b = input('목록2:').split()
    print(findMatch(a, b))
    if i != 2:
        print('**********')

# 결선투표
# def findWinner(a, b, c):
#     if a >= b+c:
#         return a
#     elif a < b+c:
#         m = max(b,c)
#         return m
#
# import sys
#
# for i in range(4):
#     print('득표수: ', end='')
#     a,b,c = map(int , sys.stdin.readline().split())
#     print(findWinner(a,b,c),'득표자 승리!')
#     if i != 3:
#         print('**********')


