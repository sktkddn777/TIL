def self_num(num):
  res = num
  for x in str(num):
    res += int(x)
  return res

def main():
  lst = []
  for i in range(1, 10001):
    lst.append(self_num(i))
  
  for i in range(1, 10001):
    if i not in lst:
      print(i)
  return

if __name__ == '__main__':
  main()