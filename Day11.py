data = open('data11.txt').read().splitlines()
final_data = []
for line in data:
    row = []
    for char in line:
        row.append(int(char))
    final_data.append(row)
    
print(final_data)
 
count = 0
def function(df, stack, count):
    ind = [[0 for x in range(12)] for y in range(12)]
    A = len(stack)
    keep_going = True
    for i in range(len(df)):
        for j in range(len(df[0])):
            if df[i][j] > 9 and (i,j) not in stack:
                stack.append((i,j))
                ind[i+1][j+2] += 1
                ind[i+2][j+2] += 1
                ind[i+2][j+1] += 1
                ind[i+2][j] += 1
                ind[i+1][j] += 1
                ind[i][j] += 1
                ind[i][j+1] += 1
                ind[i][j+2] += 1
                count += 1
                
    for i in range(len(df)):
        for j in range(len(df[0])):
            df[i][j] += ind[i+1][j+1]
            
    if len(stack) == A:
        keep_going = False
        
    return df, stack, keep_going, count
    
def do_one_step(df, count):
    for i in range(len(df)):
        for j in range(len(df[0])):
            df[i][j] += 1
    for row in df:
        print(row)
    print()
    stack = []
    keep_going = True
    while keep_going:
        for row in df:
            print(row)
        print()
        (df, stack, keep_going, count) = function(df, stack, count)
    for i in range(len(df)):
        for j in range(len(df[0])):
            if df[i][j] > 9:
                df[i][j] = 0
    return df, count

count2 = 0
i = 0
while count2 - count < 100:
    something, count2 = do_one_step(final_data, count)
    i += 1

print(i)