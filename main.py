def mult_3(li):
  result = []
  for num in li:
    if num%3 == 0:
      result.append(num)
  return result

def make_list(n):
  result = []
  i = 2
  while i <= n*2:
    result.append(i)
    i += 2
  return result
    

