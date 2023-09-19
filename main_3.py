## in-class solutions
#1
li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]
print(li[1 : 6])

#2
li = [4, 2, 6, 3, 5, 8, 3, 9, 7, 1]
print(li[2 : : 3])

#3
def squares(li):
  result = []
  for num in li:
    result.append(num ** 2)
  return result

#4
def squares_lc(li):
  return [num ** 2 for num in li]

#5
def squares_odd(li):
  result = []
  for num in li:
    if num % 2 != 0:
      result.append(num ** 2)
  return result

#6
def squares_odd_lc(li):
  return [num ** 2 for num in li if num % 2 != 0]

#7
def dot_product(l1, l2):
  result = 0
  for i in range(len(l1)):
    result += l1[i] * l2[i]
  return result

#8 
def positive_integers(n):
  result = []
  for i in range(1, n + 1):
    result.append(i)
  return result

#9 
def positive_integers_lc(n):
  return [i for i in range(1, n + 1)]

#10
def reverse(li):
  for i in range(len(li) // 2):
    li[i], li[len(li) - 1 - i] = li[len(li) - 1 - i], li[i]


