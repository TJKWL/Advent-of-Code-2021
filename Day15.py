#data = open('data15.txt').read().splitlines()
data = open('test.txt').read().splitlines()


final_data = []
for elmt in data:
    row = []
    for char in elmt:
        row.append(int(char))
    final_data.append(row)

score_matrix = [[0 for x in range(len(final_data))] for y in range(len(final_data[0]))]

score_matrix[0][0] = 0

for i in range(1, len(final_data)):
    score_matrix[i][0] = score_matrix[i-1][0] + final_data[i][0]
    
for j in range(1, len(final_data[0])):
    score_matrix[0][j] = score_matrix[0][j-1] + final_data[0][j]

for i in range(1, len(final_data)):
    for j in range(1, len(final_data[0])):
        score_matrix[i][j] = min(score_matrix[i-1][j], score_matrix[i][j-1]) + final_data[i][j]

new_data = [[0 for x in range(5*len(final_data))] for y in range(5*len(final_data))]


# =============================================================================
# new_data += new_data + new_data + new_data + new_data
# =============================================================================

a = len(final_data)

for x in range(5):
    for y in range(5):
        for i in range(a):
            for j in range(a):
                new_data[(a*x + i)][a*y + j] = final_data[i][j] + x + y
                if new_data[a*x + i][a*y + j] > 9:
                    new_data[a*x + i][a*y + j] -= 9
                    
b = len(new_data)
# =============================================================================
# for row in new_data:
#     print(row)
# =============================================================================


score_matrix = [[0 for x in range(b)] for y in range(b)]

unvisited = [(i,j) for i in range(b) for j in range(b)]











 
