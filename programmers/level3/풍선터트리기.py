def solution(a):
  balloon_dic = dict.fromkeys(a, 0)
  stack = []

  for key in balloon_dic.keys():
    if len(stack) == 0:
      stack.append(key)

    else:
      if key > stack[-1]:
        balloon_dic[key] += 1
      else:
        while key > stack[-1]:
          balloon_dic[stack[-1]] += 1
          if balloon_dic[stack[-1]] == 2:
            stack.pop()
          if len(stack) == 0:
            break
      
      stack.append(key)
  print(stack)

solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])