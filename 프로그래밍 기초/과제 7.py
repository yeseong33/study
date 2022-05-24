# 어구전철 찾기

def find_anagrams(l):
    s = list(set(l))  # 인수 리스트 안의 중복 요소 제거
    s_sort =[]

    # s 리스트 안의 단어를 정렬해 같은지 비교 할 수 있게 만들었다.
    for i in range(len(s)):
        k = list(s[i])
        k.sort()
        t = ''
        for j in range(4):
            t += k[j]
        s_sort.append(t)

    # 정렬된 문자의 개수가 1 이상이라는 것은 어구전철이 적어도 하나 존재한다는 의미이다.
    # 어구전철이 존재하는 즉, 카운트 수가 1 이상인 값과 이후 인덱스의 요소와 비교해 값이 같은
    # 인덱스를 s 에서 찾아 출력한다. 비교한 이후에는 값이 for 루프가 돌면서 중복되므로
    # 비교한 값은 ''로 값을 바꿔준다. 비교하는 키 문자는 이 출력에서 제외되므로 따로 한번 출력
    # 하면서 동시에 \n 기능을 하는 출력기능을 넣는다.

    for i in range(len(s)):
        if s_sort.count(s_sort[i]) > 1:
            for j in range(i+1, len(s)):
                if s_sort[i] == s_sort[j] and s_sort[i] != '':
                    print(s[j], end=' ')
                    s_sort[j] = ''
            if s_sort[i] != '':
                print(s[i])


find_anagrams(["0952", "5239", "1270", "8581", "7458", "3414", "7906", "2356", "4360", "3491",
 "6232", "5927", "2735", "2509", "5849", "8457", "9340", "1858", "8602", "5784"])
find_anagrams(['1112','1112','1211','2111','1211','1121','1112'])
find_anagrams(['1111','1111','1111','1111'])
find_anagrams(['0000','7890'])
find_anagrams([])


