data = open('data1.txt', 'r').read().split('\n')

n=0

for i in range(1, len(data)):
    if int(data[i]) > int(data[i-1]):
        n+=1
        
print(n)
m=0

for i in range(0,len(data)-3):
    if int(data[i]) + int(data[i+1]) + int(data[i+2]) < int(data[i+1]) + int(data[i+2]) + int(data[i+3]):
        m+=1
        
print(m)