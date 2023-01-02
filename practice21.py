# class Student:
#     count = 0
#
#
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#
#
#         #클래스 변수 설정
#         Student.count += 1
#         print(f"{Student.count}번째 학생이 생성되었습니다.")
#
#
#
# student = [
#     Student("윤인성", 87, 98, 88, 95),
#     Student("연하진", 86, 97, 87, 94),
#     Student("구지연", 76, 96, 94, 90),
#     Student("나선주", 75, 95, 93, 89),
#     Student("윤명원", 74, 94, 92, 88),
#            ]
#
# print()
# #클래서 내부와 외부에서 클래스 변수에 접근할 때는 모두 Student.count 형태를(클래스이름, 변수이름)사용합니다.
# print(f"현재 생성된 총 학생 수는 {Student.count}명입니다.")
#
#
# ######################################################################################################
#
# class Student:
#     count = 0
#     students = []
#
#
#     @classmethod
#     def print(cls):
#         print("------학생 목록-------")
#         print("이름\t총점\t평균")
#         #cls.student 매개변수로 받은 cls를 활용한다. Student.students라고 해도 상관 없다.
#         for student in cls.students:
#             print(str(student))
#         print("----- ---------- -----")
#
#
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#         Student.count += 1
#         Student.students.append(self)
#
#     def get_sum(self):
#         return self.korean + self.math +\
#             self.english + self.science
#
#
#     def get_average(self):
#         return self.get_sum() / 4
#
#     def __str__(self):
#         return ""
#
#
# print("블라블라 등등등 ")
#





#######################################################################################################


#상속
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("parent 클래스의 __init()__메소드가 호출되었습니다.")
    def test(self):
        print("parent 클래스의 test() 메소드입니다.")




class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")



# 자식 클래스의 인스턴스를 생성하고 부모의 메소드를 호출합니다.
child = Child()
child.test()
print(child.value)



#오버라이딩
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("#### 내가 만든 오류가 생성되었어요!")
    def __str__(self):
        return "오류가 발생했어요"

raise CustomException














