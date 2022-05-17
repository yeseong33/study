def isisogram(x):
    def loop(i):
        if i < len(x):
            if x[i] in x[i+1:]:
                return False
            else:
                return loop(i+1)
        else:
            return True
    return loop(0)


# print(isisogram(''))
# print(isisogram('seoul'))
# print(isisogram('korea'))
# print(isisogram('playground'))
# print(isisogram('uncopyrightables'))
# print(isisogram('aha'))
# print(isisogram('jeju'))
# print(isisogram('apple'))
# print(isisogram('jazz'))
# print(isisogram('bluenote'))


def isnagram(word1, word2):
    w1 = list(word1)
    w2 = list(word2)
    while w1 != [] :
        if len(w1) != len(w2):
            return False
        elif w1[0] in w2:
            w2.remove(w1[0])
            w1 = w1[1:]
        else:
            return False
    return True

# print(isnagram('silent', 'listen'))
# print(isnagram('silent', 'listens'))
# print(isnagram('elvis', 'lives'))
# print(isnagram('restful', 'fluster'))
# print(isnagram('restfully', 'fluster'))


def isanagram(word1, word2):
    while word1 != '':
        if word1[0] in word2:
            a = word2.find(word1)
            word1 = word1[1:]
            word2 = word2[:a] + word2[a+1:]
        else:
            return False
    return word2 == ''


# print(isanagram('',''))                 # True
# print(isanagram('z','z'))               # True
# print(isanagram('zz','z'))              # False
# print(isanagram('z','zz'))              # False
# print(isanagram('silent','listen'))     # True
# print(isanagram('silent','listens'))    # False
# print(isanagram('elvis','lives'))       # True
# print(isanagram('restful','fluster'))   # True
# print(isanagram('restfully','fluster')) # False
# print(isanagram('문전박대','대박전문'))      # True

def isanagram(word1, word2):
    while word1 != '':
        if word1[0] in word2:
            index = word2.find(word1[0])
            word1 = word1[1:]
            word2 = word2[:index] + word2[index + 1:]
        else:
            return False
    return word2 == ''

# Test code
# print(isanagram('',''))                 # True
# print(isanagram('z','z'))               # True
# print(isanagram('zz','z'))              # False
# print(isanagram('z','zz'))              # False
# print(isanagram('silent','listen'))     # True
# print(isanagram('silent','listens'))    # False
# print(isanagram('elvis','lives'))       # True
# print(isanagram('restful','fluster'))   # True
# print(isanagram('restfully','fluster')) # False
# print(isanagram('문전박대','대박전문'))      # True
# print(isanagram('asdk','asdf'))




def find_2st(filename, x):
    infile = open(filename, 'r',  encoding='UTF8')
    outfile = open('result.txt','w')
    text = infile.read()
    p = text.find(x)
    posision = text.find(x, p+1)
    if posision == -1:
        outfile.write(x+' is not found.\n')
    else:
        outfile.write(x+' is at '+ str(posision)+' the 2st time.\n')
    outfile.close()
    infile.close()
    print('Done')

# find_2st('article.txt', 'computer')
# find_1st('article.txt', 'Whole Earth')
# find_1st('article.txt', 'Apple')
# find_1st('article.txt', 'apple')

def find_last(filename, x):
    infile = open(filename, 'r',  encoding='UTF8')
    outfile = open('result.txt','w')
    text = infile.read()
    lp = -1
    posision = text.find(x)
    while posision != -1:
        lp = posision
        posision = text.find(x, posision+1)
    if lp == -1:
        outfile.write(x+' is not found.\n')
    else:
        outfile.write(x+' is at '+ str(lp)+' the last time.\n')
    outfile.close()
    infile.close()
    print('Done')


# find_last('article.txt', 'computer')
# find_last('article.txt', 'Whole Earth')
# find_last('article.txt', 'Apple')
# find_last('article.txt', 'apple')


def find_all(filename, x):
    infile = open(filename, 'r',  encoding='UTF8')
    outfile = open('result.txt','a')
    text = infile.read()
    posision = text.find(x)
    order = []
    order.append(posision)
    while posision != -1:
        posision = text.find(x, posision+1)
        order.append(posision)
    if order == [-1] :
        outfile.write(x+' is not found.\n')
    else:
        k = ''
        for i in order[:-1]:
            if i == order[-2]:
                k += str(i)+'.'
            else:
                k += str(i)+', '
        outfile.write('at '+ k+'\n')
    outfile.close()
    infile.close()
    print('Done')


# find_all('article.txt', 'computer')
# find_all('article.txt', 'Whole Earth')
# find_all('article.txt', 'Apple')
# find_all('article.txt', 'apple')



# 정리해보기 더 간결하게
def find_all_count(filename, x):
    infile = open(filename, 'r',  encoding='UTF8')
    outfile = open('result.txt','a')
    text = infile.read()
    posision = text.find(x)
    order = []
    order.append(posision)
    while posision != -1:
        posision = text.find(x, posision+1)
        order.append(posision)
    if order == [-1] :
        outfile.write(x+' is not found.\n')
    else:
        k = ''
        for i in order[:-1]:
            if i == order[-2]:
                k += str(i)+'.'
            else:
                k += str(i)+', '
        outfile.write(str(len(order)-1)+' time(s)'+'\n')
    outfile.close()
    infile.close()
    print('Done')


# find_all_count('article.txt', 'computer')
# find_all_count('article.txt', 'Whole Earth')
# find_all_count('article.txt', 'Apple')
# find_all_count('article.txt', 'apple')










