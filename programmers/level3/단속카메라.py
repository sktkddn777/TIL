

# def solution(routes):
#   check = [0] * len(routes)
#   routes.sort(key=lambda x:x[1])
#   print(routes)
#   answer = 0
#   for i in range(len(routes)):
#     if check[i] == 0:
#       camera = routes[i][1]
#       answer += 1
    
#     for x in range(i+1, len(routes)):
#       if routes[x][1] >= camera >=routes[x][0] and check[x] == 0:
#         check[x] = 1

#   return answer

def solution(routes):
  answer = 0
  camera = -30001
  routes.sort(key=lambda x:x[1])
  for route in routes:
    if route[0] > camera:
      answer += 1
      camera = route[1]
  
  return answer
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

