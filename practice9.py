name_dict = dict()
num_list =[]

idx = 0

idx += 1
name_dict[idx] ='김연수'

idx += 1
name_dict[idx] = '이지혜'

idx += 1
name_dict[idx] = '고연재'

idx += 1
name_dict[idx] = '박성빈'

idx += 1
name_dict[idx] = '김성일'


print(name_dict)
print(name_dict.keys())
print(name_dict.values())

temp = list(name_dict.values())
temp_sort = temp
temp_sort.sort()

idx = 0
for value in temp_sort:
    idx += 1
    print(f'{value}님의 출석번호는 {idx}이고, 가입순서는 {temp.index(value)+1}')