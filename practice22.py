# class Student:
#     def __init__(self, name, korean, math, english, science):
#         self.name = name
#         self.korean = korean
#         self.math = math
#         self.english = english
#         self.science = science
#
#
#
#     def get_sum(self):
#         return self.korean + self.math + self.english + self.science
#
#
#
#     def get_average(self):
#         return self.get_sum() / 4
#
#
#     def to_string(self):
#         return "{}\t\t{}\t\t\{}".format(
#             self.name,
#             self.get_sum(),
#             self.get_average()
#
#
#
#
#             )
#
# students = [
#         Student("윤인성", 87, 98, 88, 95),
#         Student("연하진", 92, 98, 96, 98),
#         Student("구지연", 76, 96, 94, 90),
#         Student("나선주", 98, 92, 96, 92),
#         Student("윤아린", 95, 98, 98, 98),
#         Student("윤명월", 64, 88, 92, 92)
#            ]
#
#
#
# print("이름\t\t", "총점\t", "평균\t\t", sep="\t")
# for student in students:
#     print(student.to_string())

#
# class Student:
#     def __init__(self):
#         pass
#
#
#
# student = Student()
#
# print("isinstance(student, Student):", isinstance(student, Student))
#
#
# class Human:
#     def __init__(self):
#         pass

#
# class Student(Human):
#     def __init__(self):
#         pass
#
#
# student = Student()
#
# print("isinstance(student, Human):", isinstance(student, Human))
#
#
# class Student:
#     def study(self):
#         print("공부합니다.")
#
# class Teacher:
#     def teach(self):
#         print("학생을 가르칩니다.")


# classroom = [Student(), Student(), Teacher(), Student(), Student()]
#
# for person in classroom:
#     if isinstance(person, Student):
#         person.study()
#     elif isinstance(person, Teacher):
#         person.teach()

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self. damage = damage
        print(f"{self.name}유닛이 생성 됐습니다.")
        print(f"체력{self.hp}, 공격력{self.damage}")


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

#Unit 클래스 매개변수는 3개다. 고로 3개를 채워야 된다.

wraith = Unit("레이스", 80, 5)
print(f"유닛이름: {wraith.name} 공격력:{wraith.damage}")
wraith2 = Unit("레이스", 80, 5)


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self. damage = damage
        print(f"{self.name}유닛이 생성 됐습니다.")
        print(f"체력{self.hp}, 공격력{self.damage}")

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print(f"{self.name}: {location}방향으로 적군을 공격합니다.[공격력 {self.damage}]")

    def damaged(self, damage):

        print(f'{self.name}: {damage} 데미지를 입었습니다.')
        self.hp -= damage
        print(f'{self.name}: 현재 체력은 {self.hp}입니다.')
        for i in range(self.hp):

                    if self.hp <= 0:
                        print(f'{self.name}: 파괴 되었습니다.')


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)





















