def check_number_with_comma(s):
    def loop(s):
        (front, comma, rest) = s.partition(",")
        return len(front) == 3 and comma == ',' and loop(rest) or \
               len(front) == 3 and comma == ''


    (front, comma, rest) = s.partition(",")
    # return len(front) == 3 and int(front) >= 100 and (comma == '' or (comma == ',' and loop(rest))) or \
    #        len(front) == 2 and int(front) >= 10 and (comma == '' or (comma == ',' and loop(rest))) or \
    #        len(front) == 1 and int(front) != 0 and (comma == '' or (comma == ',' and loop(rest)))
    return len(front) == 3 and int(front) >= 100 and (comma == '' or loop(rest)) or \
           len(front) == 2 and int(front) >= 10 and (comma == '' or loop(rest)) or \
           len(front) == 1 and int(front) != 0 and (comma == '' or loop(rest))


print(check_number_with_comma("")) # False
print(check_number_with_comma("1")) # True
print(check_number_with_comma("0")) # False
print(check_number_with_comma("11")) # True
print(check_number_with_comma("01")) # False
print(check_number_with_comma("111")) # True
print(check_number_with_comma("011")) # False
print(check_number_with_comma("1111")) # False
print(check_number_with_comma("0111")) # False
print(check_number_with_comma("1,111")) # True
print(check_number_with_comma("1,000,011")) # True
print(check_number_with_comma("1,000,011,001")) # True
print(check_number_with_comma("01,000,011,001")) # False
print(check_number_with_comma("1,00,011,001")) # False
print(check_number_with_comma("1,000,11,001")) # False
print(check_number_with_comma("1,000,011,1")) # False
