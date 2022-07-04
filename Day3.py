data = open('data3.txt', 'r').read().split('\n')

gamma = []

for i in range(len(data[0])):
    n=0
    m=0
    for line in data:
        if int(line[i]) == 0:
            n+=1
        if int(line[i]) == 1:
            m+=1
    if n>m:
        gamma.append('0')
    else:
        gamma.append('1')      

g = int(''.join(gamma),2)

pow_consumption = g * (2**(len(gamma)) - 1 - g)

print(pow_consumption)



def oxygen_gen(array, i):
   vec = []
   n=0
   m=0
   for line in array:
       if int(line[i]) == 0:
           n+=1
       if int(line[i]) == 1:
           m+=1
   if n>m:
       vec = [line for line in array if int(line[i]) == 0]
   else:
       vec = [line for line in array if int(line[i]) == 1]
                   
   return vec

k = oxygen_gen(data,0)
l = [line for line in data if line not in k]

for i in range(1, len(data[0])):
    k = oxygen_gen(k,i)
    if len(k) == 1:
        break
       
for j in range(1, len(data[0])):
    l = [line for line in l if line not in oxygen_gen(l,j)]
    if len(l) == 1:
        break

print(int(k[0],2)*int(l[0],2))