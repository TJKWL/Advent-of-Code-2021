data = open("data4.txt").read().split('\n')

test_numbers = data[0]
data.remove(data[0])

final_data = []

for i in range(100):
    new_row = []
    for j in range(5):
        data_to_add = [data[6*i + j + 1]]
        better_format = [s.split() for s in data_to_add]
        even_better_format = [int(s) for s in better_format[0]]
        new_row.append(even_better_format)
    final_data.append(new_row)


tests = test_numbers.split(',')
numbers_drawn = [int(s) for s in tests]

numbers_checked = []

indicator = [[[0 for x in range(5)] for y in range(5)] for z in range(100)]

for i in range(21):
    numbers_checked.append(numbers_drawn[i])
    #check each matrix
    for j in range(100):
        #check each row
        for k in range(5):
            for n in range(5):
                if final_data[j][k][n] == numbers_drawn[i]:
                    indicator[j][k][n] = 1
            check = all(item in numbers_checked for item in final_data[j][k])
            if check == True:
                print(final_data[j][k], j, k)
                
        #check each column
        for l in range(5):
            check = all(item in numbers_checked for item in [final_data[j][n][l] for n in range(5)])
            if check == True:
                print([final_data[j][n][l] for n in range(5)])
                
total = 0

for i in range(5):
    for j in range(5):
        if indicator[62][i][j] == 0:
            total += final_data[62][i][j]
                
print(total)

N = 84

numbers = [numbers_drawn[i] for i in range(N)]

count = 0
#check each matrix
for j in range(100):
    Bingo = False
    #check each row
    for k in range(5):
        check1 = all(item in numbers for item in final_data[j][k])
        if check1 == True:
            Bingo = True
    #check each column
    for l in range(5):
        check2 = all(item in numbers for item in [final_data[j][n][l] for n in range(5)])
        if check2 == True:
            Bingo = True
                   
    if Bingo == True:
        count += 1
        print("BINGO", j)
        
total2=0

for i in range(5):
    for j in range(5):
        if final_data[84][i][j] not in numbers:
            total2 += final_data[84][i][j]
            
print(total2)