import math

def park_fee(fees, time):
    base_time = fees[0]
    base_fee = fees[1]
    danwe_time = fees[2]
    danwe_fee = fees[3]
    if time <= base_time:
        return base_fee
    
    return base_fee + math.ceil((time - base_time) / danwe_time) * danwe_fee
    

def solution(fees, records):
    car_dic = {}
    for record in records:
        time, car, status = record.split()     
        h, m = time.split(':')
        time = int(h) * 60 + int(m)
        if car not in car_dic:
            car_dic[car] = [time]
        else:
            car_dic[car].append(time)
    car_dic = dict(sorted(car_dic.items()))
    for car in car_dic:
        if len(car_dic[car]) % 2 != 0:
            car_dic[car].append(1439)
    car_time_dic = {c:0 for c in car_dic}
    for c in car_dic:
        for i in range(0, len(car_dic[c]), 2):
            car_time_dic[c] += (car_dic[c][i+1] - car_dic[c][i])
    answer = []

    for c in car_time_dic:
        answer.append(park_fee(fees, car_time_dic[c]))

    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))