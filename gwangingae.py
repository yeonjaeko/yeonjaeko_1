# random_pop.py
import random #c모듈을 파이썬으로 가져오고 싶을때 쓰는 명령어? import
def random_pop(data): #랜덤함수
    number = random.randint(0, len(data)-1) #number의 사이즈를 지정하는 걸로 보임
    return data.pop(number) #넘버에 지정된 사이즈 결과값을 돌려주는 리턴 명령어

if __name__ == "__main__": # __name__이라는 변수의 값이 __main__인지 확인하는 코드. 이 식으로 프로그램의 시작을 선언하는 것 같다.
    data = ['임홍선', '고연재', '이현도', '노도현', '강민영', '장은희', '정연우', '주민석',
            '최지혁', '정철우', '김연수', '이여름', '박시형', '김기태', '김성일', '김재일',
            '오송화', '이보라', '박성빈', '이범규', '박규환', '이지혜', '이소윤', '류가미',
            '임영효', '박의용', '김명은', '임성경']

    print("분리수거 2명:")
    data: print(random_pop(data))
    data: print(random_pop(data))
    print("쓸기 1명:")
    data: print(random_pop(data))
    print("닦기 1명:")
    data: print(random_pop(data))


