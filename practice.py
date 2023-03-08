#################################################################

# def digitize(n):
#     arr = []
#     for x in range(0, len(str(n))):
#         arr += str(n)[x]
#     arr.reverse()
#     arr = list(map(int, arr))
#     return arr
#
#
# def digitizeTwo(n):
#     return list(map(int, str(n)[::-1]))
#
#
# result = digitizeTwo(32564)
# print(result)

###############################################################

# # def summation(num):
# #     answer = 0
# #     for x in range(0, num+1):
# #         answer += x
# #     return answer
#
# def summation(num):
#     return sum(range(num + 1))
#
#
# result = summation(8)
# print(result)

################################################################

# def sum_mix(arr):
#     return sum(list(map(int, arr)))
#
#
# result = sum_mix((9, 3, '7', '3'))
# print(result)

#######################################################################

# def feast(beast, dish):
#     return beast[0] == dish[0] and beast[-1] == dish[-1]
#
#
# beast = 'hello'
# dish = 'hoo'
# if beast[0] == dish[0] and beast[-1] == dish[-1]:
#     print('yes')
# else:
#     print('no')

######################################################################

# def filter_list(l):
#     """return a new list with the strings filtered out"""
#     newL = []
#     for x in l:
#         if type(x) is int:
#             newL.append(x)
#     return newL
#
#
# result = filter_list([1, 2, 'a', 'b', 4])
# print(result)

#####################################################################

# def create_phone_number(n):
#     phone_number = ''.join([str(item) for item in n])
#     return "({}) {}-{}".format(phone_number[0:3], phone_number[3:6], phone_number[6:10])
#
# # Best Solution using unpacking of an operator (*)
# # def create_phone_number(n):
# #     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
#
#
# result = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# result2 = "{} + {} = {}".format(result[0:2], result[3:6], result[7:10])
# print(result)

######################################################################

# def find_it(seq):
#     for i in seq:
#         if seq.count(i) % 2 != 0:
#             return i
#
#
# result = find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
# print(result)

############################################################################

# # Find shortest word in a string
#
# # converted to list, split the list and mapped it by length.
# def find_short(s):
#     shortList = s.split(' ')
#     l = len(min(shortList, key=len))
#     return l
#
#
# s = 'Ifhdsjfs fdsfsdf sfgfff sfs'
# result = find_short(s)
# print(result)
#
# # shorter method
#
# def find_short(s):
#     return min(len(x) for x in s.split())

############################################################################


