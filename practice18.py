import random


def unannounced_inspection (worker2, week_sum2):
  print("고용노동부에서 근로계약 불시검문을 왔습니다.")
  print("아르바이트생들과 면담이 시작됐습니다.")
  a = random.randint(1, 3)
  if a == 1:
      b = random.randint(1, 5)
      unhappy_worker = worker2 // b
      print(f"{unhappy_worker}명의 아르바이트생이 공무원에게 불만을 토로했습니다.")
      print("파견 공무원이 해당 아르바이트생들의 고용계약서를 확인하고 있습니다.")
      c = random.randint(1, 3)
      if c == 1:
          pm_unhappy_worker = (unhappy_worker * 0.15) * 5000000
          print(f"{pm_unhappy_worker}명의 아르바이트생의 고용계약서에서 문제가 발견됐습니다.")
          week_sum2 -= pm_unhappy_worker
          print(f"{pm_unhappy_worker}의 손해를 봤습니다.")
          return pm_unhappy_worker

      else:
         print("고용계약서에 아무런 문제가 없습니다.")
         return week_sum2

  else:
       return week_sum2




