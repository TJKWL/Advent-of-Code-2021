data = open('data6.txt').read().split(',')
final_data = [int(s) for s in data]

indicator = [0,0,0,0,0,0,0,0,0]

for i in range(len(final_data)):
    for j in range(8):
        if final_data[i] == j:
            indicator[j] += 1
            
for n in range(256):
    a = indicator[0]
    for i in range(len(indicator)-1):
        indicator[i] = indicator[i+1]
    indicator[6] += a
    indicator[8] = a
    
print(sum(indicator))