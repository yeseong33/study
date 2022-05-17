# def validclock24(time):
#     (hour, colon, minute) = time.partition(":")
#     if len(hour) == 2 and len(minute) == 2:
#         if 0 <= int(hour)<24 and 0 <= int(minute) <= 59 or\
#                 int(hour) == 24 and int(minute) == 0:
#             return True
#         else:
#             return False
#     else:
#         return False

# def validclock24(time):
#     (hour, colon, minute) = time.partition(":")
#     return (len(hour) and len(minute)) == 2 and\
#            0 <= int(hour) <24 and 0<= int(minute)<=59 or\
#            int(hour) == 24 and int(minute) == 0
## True or False로 표현되는 식은 논리식으로만 표현하는게 간결하다.



#
# # Test code
print(validclock24("00:00"))  # True
print(validclock24("00:30"))  # True
print(validclock24("09:58"))  # True
print(validclock24("12:15"))  # True
print(validclock24("23:59"))  # True
print(validclock24("24:00"))  # True
print(validclock24("7:07"))   # False
print(validclock24("07:121")) # False
print(validclock24("13:4"))   # False
print(validclock24("00:60"))  # False
print(validclock24("24:01"))  # False
print(validclock24("25:10"))  # False



# def clock24to12(time):
#     (hour, colon, minute) = time.partition(":")
#     IH = int(hour)
#     IM = int(minute)
#
#     if len(hour) == 2 and len(minute) == 2:
#         if (0 <= IH < 12 or IH == 24) and 0 <= IM <= 59:
#             if IH == 0 or IH == 24:
#                 IH = 12
#             time = str(IH)+':'+minute
#             am = time+'am'
#             return am
#
#         elif 12 <= IH < 24 and 0 <= IM <= 59:
#             if IH == 12:
#                 IH = 24
#             time = str(IH -12)+':'+minute
#             pm = time+'pm'
#             return pm
#         else:
#             None
#
#     else:
#         return None
#
# print(clock24to12("00:00")) # "12:00am"
# print(clock24to12("00:05")) # "12:05am"
# print(clock24to12("09:58")) # "9:58am"
# print(clock24to12("11:43")) # "11:43am"
# print(clock24to12("12:08")) # "12:08pm"
# print(clock24to12("15:50")) # "3:50pm"
# print(clock24to12("20:20")) # "8:20pm"
# print(clock24to12("24:00")) # "12:00am"


# def clock24to12(time):
#     (hour, colon, minute) = time.partition(":")
#     if len(hour) == 2 and len(minute) == 2:
#         if 0 <= int(hour) < 12 and 0 <= int(minute) <= 59:
#             am = hour+':'+minute+'am'
#             return am
#         elif int(hour) == 0 and 0 <= int(minute) <= 59:
#             am = '12:'+minute+'am'
#             return am
#         elif int(hour) == 12 and 0 <= int(minute) <= 59:
#             pm = '12:'+minute+'pm'
#             return pm
#         elif 13 <= int(hour)< 24 and 0 <= int(minute) <= 59:
#             time = str(int(hour) -12)+':'+str(int(minute))
#             pm = time+'pm'
#             return pm
#         elif int(hour) == 24 and int(minute) == 0:
#             return '12:00am'
#         else:
#             None
#     else:
#         return None