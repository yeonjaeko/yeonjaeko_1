print("%10.4f" % 3.42134234)
print("%0.4f" % 3.42134234)

print("%0.6f" % 3.4213234)
print("%0.7f" % 3.4213234)

print("error is %d%%." % 98)

a = 4.24E10
print("%0.100f" % a)

a = 4.24e-10
print("%0.200f" % a)

a = 0o177
print("%0.150f" % a)

a = 0x8ff
print("%10.200f" % a)


print("10진수 2진수 8진수 16진수")
for i in range(1,11):
     bin1 = bin(i)
     oct1 = oct(i)
     hex1 = hex(i)
     print(f'{i}',  '   ',bin1,'  ',oct1,' ',hex1 )

