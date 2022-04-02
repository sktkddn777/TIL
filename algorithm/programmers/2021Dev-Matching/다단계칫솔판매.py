import math

def solution(enroll, referral, seller, amount):
  relation = dict(zip(enroll, referral))
  people = {key: 0 for key in enroll}
 
  for i in range(len(seller)):
    money = amount[i] * 100
    cur = seller[i]
    while cur != '-':
      if money > 9:
        people[cur] += math.ceil(money * 0.9)
        money *= 0.1
        cur = relation[cur]
      else:
        people[cur] += int(money)
        break

  return list(people.values())


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))