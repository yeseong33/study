def find_1st(filename, x):
    infile = open(filename, 'r')
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

    