expressions = input()

expression_lst = expressions.split('-')

total = 0
for i in range(1, len(expression_lst)):
  temp = expression_lst[i].split('+')
  temp = [int(i) for i in temp]
  total -= sum(temp)

expression = expression_lst[0].split('+')
expression = [int(i) for i in expression]
print(total + sum(expression))