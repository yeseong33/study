# num = int(input())
# k = 0
# while k != num:
#     s = input()
#     s1 = s.split()
#     k += 1
#     print('Case #{}:'.format(k),int(s1[0])+int(s1[1]))


num = int(input())
k = 0
while k != num:
    s = input()
    s1 = s.split()
    k += 1
    print('Case #{}: {} + {} ='.format(k, int(s1[0]), int(s1[1])),int(s1[0])+int(s1[1]))


