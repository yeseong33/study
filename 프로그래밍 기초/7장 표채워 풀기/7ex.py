# 봉지 2, 3, 5
# 주문 2키로 이상만
# 봉지의 수가 최소가 되도록 포장
# 18 = 5 5 5 3


def minbegs(kg):
    kg_5 = kg // 5
    kg_3 = kg % 5 // 3
    kg_2 = kg % 5 % 3
    b = kg_2 + kg_3 + kg_5
    return b


def minbegs(kg):
    if kg > 1:
        if kg == 2 or kg == 3 or kg == 5
            return 1
        else:
            smallest = minbegs(n-2)
            if n > 4:
                smallest = min(smallest, minbegs(kg-3))
            if n > 6:
                smallest = min(smallest, minbegs(kg-5))
        return 1 + smallest
    else:
        return 0

