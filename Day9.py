data = open('data9.txt').read().split('\n')
#data = ['2199943210', '3987894921', '9856789892', '8767896789','9899965678']
df = []
df.append([9 for x in range(len(data[0])+2)])

for string in data:
    row = [9]
    for char in string:
        row.append(int(char))
    row.append(9)
    df.append(row)

df.append([9 for x in range(len(data[0])+2)])

# =============================================================================
# for row in df:
#     print(row)
# =============================================================================

low_points = []
lows = set()

indicator = [[0 for x in range(len(df[0]))] for y in range(len(df))]

for i in range(1, len(df)-1):
    for j in range(1, len(df[0])-1):
        if df[i][j] < df[i-1][j]:
            indicator[i][j] += 1
        if df[i][j] < df[i+1][j]:
            indicator[i][j] += 1
        if df[i][j] < df[i][j-1]:
            indicator[i][j] += 1
        if df[i][j] < df[i][j+1]:
            indicator[i][j] += 1
            
for i in range(len(indicator)):
    for j in range(len(indicator[i])):
        if indicator[i][j] == 4:
            low_points.append(df[i][j])
            lows.add((i,j))
                       
# =============================================================================
# print(sum(low_points) + len(low_points))
# for row in indicator:
#     print(row)
# 
# print(lows)
# =============================================================================

def f(ind, i , j, basin_set):
    basin_set.add((i,j))
    
    if df[i+1][j] != 9 and (i+1,j) not in basin_set:
        f(ind,i+1,j, basin_set)
        
    if df[i-1][j] != 9 and (i-1,j) not in basin_set:
        f(ind,i-1,j, basin_set)
        
    if df[i][j-1] != 9 and (i,j-1) not in basin_set:
        f(ind,i,j-1, basin_set)
        
    if df[i][j+1] != 9 and (i,j+1) not in basin_set:
        f(ind,i,j+1, basin_set)
        
    return basin_set

basins = []

for coords in lows:
    if not any(coords in st for st in basins):
        basins.append(f(indicator, coords[0], coords[1], set()))
        
counts = []

for st in basins:
    counts.append(len(st))
    
print(sorted(counts))

    
    
    