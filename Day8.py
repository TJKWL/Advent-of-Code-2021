data = open('data8.txt').read().split('\n')
split_data = [s.split(' | ') for s in data]


final_data = []
for i in range(len(split_data)):
    row = []
    for j in range(2):
        row.append(split_data[i][j].split(' '))
    final_data.append(row)

count = 0

for row in final_data:
    for elmt in row[1]:
        if len(elmt) in [2, 3, 4, 7]:
            count += 1
print(count)

def find_segments(lst):  
    for code in lst:
        if len(code) == 2:
            one = code
        elif len(code) == 3:
            seven = code
    for code in lst:
        if len(code) == 4:
            four = code
    for char in seven:
        if char not in one:
            top = char
    for code in lst:
        if len(code) == 5:
            if (one[0] in code) and (one[1] in code) and (top in code):
                three = code
    for char in three:
        if char in four and char not in one:
            middle = char
    for char in three:
        if char not in seven and char not in middle:
            bottom = char          
    for char in four:
        if char not in middle and char not in one:
            topleft = char
    for code in lst:
        if len(code) == 5:
            if top in code and middle in code and bottom in code and topleft in code:
                for char in code:
                    if char not in [top, middle, bottom, topleft]:
                        bottomright = char
    for char in one:
        if char not in bottomright:
            topright = char
    for code in lst:
        if len(code) == 7:
            for char in code:
                if char not in [top, middle, bottom, topleft, bottomright, topright]:
                    bottomleft = char
                    
    return [top, middle, bottom, topleft, bottomright, topright, bottomleft]

final_numbers = []

for row in final_data:
    segments = find_segments(row[0])    
    number = []
    for code in row[1]:
        if len(code) == 2:
            number.append(1)
        elif len(code) == 3:
            number.append(7)
        elif len(code) == 4:
            number.append(4)
        elif len(code) == 7:
            number.append(8)
        elif len(code) == 6:
            if segments[1] not in code:
                number.append(0)
            elif segments[5] not in code:
                number.append(6)
            else:
                number.append(9)
        else:
            if segments[3] in code:
                number.append(5)
            elif segments[4] in code:
                number.append(3)
            else:
                number.append(2)
    final_numbers.append(number)
  
count = 0 
for number in final_numbers:
    for i in range(len(number)):
        count += number[i] * 10**(len(number) - i - 1)

print(count)