def find_1st(filename, x):
    infile = open(filename, 'r', encoding='utf-8')
    text = infile.read()
    infile.close()
    position = text.find(x)
    outfile = open('result.txt','w')
    if position == -1:
        outfile.write(x+' is not found. \n')
    else:
        outfile.write(x +' is at '+str(position) + ' the 1st time. \n')
    outfile.close()
    print('Done')

find_1st('article.txt', 'a')