# 한 사람이 돈이 5000원이 있는데 사탕의 가격이 120원이라면 최대로 살수 있는 사탕의 수는 몇개인지
# 알아보는 프로그램

myMoney = int(input('가지고 있는 돈 : '))
candyPrice = 120
numCandies = myMoney//candyPrice
print('살 수 있는 사탕의 개수 : ',candyPrice)

# 최대로 살 수 있는 사탕을 구입하고 남은 돈
exMoney = myMoney%candyPrice
print('사탕을 사고 남은 돈 : ',exMoney)