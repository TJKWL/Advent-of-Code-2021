import re

data = open('data5.txt').read().split()
df = [re.split(',|->', data[i]) for i in range(len(data))]
final_data = []

for i in range(int(len(df)/3)):
    new_row = []
    new_row.append([int(s) for s in df[3*i]])
    new_row.append([int(s) for s in df[3*i + 2]])
    final_data.append(new_row)
    
def find_points_between_two_numbers(a, b):
    d = a - b
    if a < b:
        return [a+i for i in range(-d+1)]   
    if b < a:
        return [b+i for i in range(d+1)]
  
def find_points_between_two_points(pnt1, pnt2):
    a = find_points_between_two_numbers(pnt1[0], pnt2[0])
    b = find_points_between_two_numbers(pnt1[1], pnt2[1])
    if pnt1[0] == pnt2[0]:                      return [[pnt1[0], a] for a in find_points_between_two_numbers(pnt1[1], pnt2[1])]
    if pnt1[1] == pnt2[1]:                      return [[a, pnt2[1]] for a in find_points_between_two_numbers(pnt1[0], pnt2[0])]
    if pnt1[0] + pnt1[1] == pnt2[0] + pnt2[1]:  return [[a[len(a) - 1 - i], b[i]] for i in range(len(a))]
    if pnt1[0] - pnt2[0] == pnt1[1] - pnt2[1]:  return [[a[i], b[i]] for i in range(len(a))]
          
indicator = [[0 for x in range(1000)] for y in range(1000)] 
for pnt in [s for coords in final_data for s in find_points_between_two_points(coords[0], coords[1])]:
    indicator[pnt[0]][pnt[1]] += 1

count = 0
for row in indicator:
    for number in row:
        if number > 1:
            count +=1
print(count)