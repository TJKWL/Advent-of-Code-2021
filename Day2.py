data = open('data2.txt').read().split('\n')

answer = [0,0]

for line in data:
    if line[0] == 'f':
        answer[1]+=int(line[8])
    if line[0] == 'u':
        answer[0]-=int(line[3])
    if line[0] == 'd':
        answer[0]+=int(line[5])
       
print(answer[0]*answer[1])

aim = 0
hor = 0
dep = 0

for line in data:
    if line[0] == 'f':
        hor += int(line[-1])
        dep += int(line[-1]) * aim
    elif line[0] == 'u':
        aim -= int(line[-1])
    elif line[0] == 'd':
        aim += int(line[-1])
        
print(hor*dep)