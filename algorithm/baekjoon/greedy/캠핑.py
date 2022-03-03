x = 1
while True:
  L, P, V = map(int, input().split())
  if L+P+V == 0:
    break
  
  res = L * (V // P)
  res += min(L, (V%P))
  
  print(f"Case {x}:", res)
  x += 1