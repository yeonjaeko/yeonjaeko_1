#
# s = "aa. bb. cc. dd. ee"
# print(f'{s}')
#
# r0 = s.split()
# r1 = s.split('.')
# r2 = s.split(sep='.')
# print(f"{r0}")
# print(f"{r1}")
# print(f"{r2}")
#
#
# # def add_many(*args):
# #   result = 0
# #   for i in args:
# #     result = result + i
# #   return result
#
# a = 1
# def vartest():
#     global a
#     a = a+1
#
# vartest()
# print(a)



f = open("C:/doit/새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

