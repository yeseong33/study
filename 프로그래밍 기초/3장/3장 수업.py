# def isinteger(s):
#     return s.isdigit() or \
#            s != '' and s[0] == '-' and s[1:].isdigit()

# def isinteger(s):
#     if s.isdigit():
#         return True
#     else:
#         if s != '-':
#             if s[0] == '' and s[1:].isdigit():
#                 return True
#             else:
#                 return False
#         else:
# #             return False
# ## True or False로 표현되는 식은 논리식으로만 표현하는게 간결하다.

# def isfloat(s):
#     (left, dot, right) = s.partition('.')
#     return dot == '' and isinteger(left) and right == '' or \
#            dot == '.' and \
#            ((left == '' or left == '-') and isinteger(right) or
#            isinteger(left) and right =='' or
#            isinteger(left) and isinteger(right))
#
# # 조건
# # '.' 일때
# # 1. 양쪽이 모두 채워짐
# # 2. 오른쪽만 채워짐
# # 3. 왼쪽만 채워짐 and 왼쪽 '-'이면서 오른쪽이 비면 안됨
# # 4. 둘다 비면 안됨
# #
# # '' 일때
# # 1. 왼쪽만 채워짐
#
#
#
# print(isfloat("2"))
# print(isfloat("-2"))
# print(isfloat(".112"))
# print(isfloat("-.112"))
# print(isfloat("3.14"))
# print(isfloat("-3.14"))
# print(isfloat("5."))
# print(isfloat("5.0"))
# print(isfloat("-777.0"))
# print(isfloat("-777."))
# print(isfloat("."))
# print(isfloat(".."))




# def isleapyear(year):
#     if year < 0:
#         return None
#     else:
#         return year % 4 ==0 and year % 100 != 0 or year % 400 == 0

# print(isleapyear(2008))
# print(isleapyear(2012))
# print(isleapyear(2016))
#
# print(isleapyear(1600))
# print(isleapyear(2000))
# print(isleapyear(2400))
#
# print(isleapyear(2013))
# print(isleapyear(2014))
# print(isleapyear(2015))
#
# print(isleapyear(2100))
# print(isleapyear(2200))
# print(isleapyear(2300))

# print(isleapyear(0))     # True
# print(isleapyear(1))     # False
# print(isleapyear(4))     # True
# print(isleapyear(2010))  # False
# print(isleapyear(2011))  # False
# print(isleapyear(2012))  # True
# print(isleapyear(2013))  # False
# print(isleapyear(2016))  # True
# print(isleapyear(1900))  # False
# print(isleapyear(2000))  # True
# print(isleapyear(2020))  # True
# print(isleapyear(2100))  # False
# print(isleapyear(2200))  # False
# print(isleapyear(2400))  # True
# print(isleapyear(-2000)) # None

# def validclock24(time):
#     (hour,colon,minute) = time.partition(':')
#     return colon == ':' and\
#         (len(hour) == 2 and len(minute) == 2) and\
#         0 <= int(hour) < 24 and 0 <= int(minute) <= 59 or \
#         int(hour) == 24 and int(minute) == 0
#
# # # Test code
# print(validclock24("00:00"))  # True
# print(validclock24("00:30"))  # True
# print(validclock24("09:58"))  # True
# print(validclock24("12:15"))  # True
# print(validclock24("23:59"))  # True
# print(validclock24("24:00"))  # True
# print(validclock24("7:07"))   # False
# print(validclock24("07:121")) # False
# print(validclock24("13:4"))   # False
# print(validclock24("00:60"))  # False
# print(validclock24("24:01"))  # False
# print(validclock24("25:10"))  # False
# print(validclock24("+5:10"))



def clock24to12(time):
    (hour, colon, minute) = time.partition(':')
    IH = int(hour)
    if 0 <= IH < 12 or IH == 24:
        if IH == 0 or IH == 24:
            IH = 12
        return str(IH)+':'+minute+'am'
    elif 12 <= IH < 24:
        if IH == 12 :
            IH = 24
        return str(IH-12)+':'+minute+'pm'
    else:
        return None

print(clock24to12("00:00")) # "12:00am"
print(clock24to12("00:05")) # "12:05am"
print(clock24to12("09:58")) # "9:58am"
print(clock24to12("11:43")) # "11:43am"
print(clock24to12("12:08")) # "12:08pm"
print(clock24to12("15:50")) # "3:50pm"
print(clock24to12("20:20")) # "8:20pm"
print(clock24to12("24:00")) # "12:00am"