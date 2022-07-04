final_data = open('data10.txt').read().splitlines()

ans1 = 0
big_stack = []
for line in final_data:
    broken = False
    stack = []
    for char in line:
        if char == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                ans1 += 57
                broken = True
                break
        if char == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                ans1 += 3
                broken = True
                break
        if char == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                ans1 += 1197
                broken = True
                break
        if char == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                ans1 += 25137
                broken = True
                break
        if char in ['(', '{', '[', '<']:
            stack.append(char)
    if broken == False:
        big_stack.append(stack)
    
counts = []
for stack in big_stack:
    count = 0
    while stack != []:
        if stack[-1] == '[':
            count *= 5
            count += 2
            stack.pop()
        elif stack[-1] == '(':
            count *= 5
            count += 1
            stack.pop()
        elif stack[-1] == '{':
            count *= 5
            count += 3
            stack.pop()
        elif stack[-1] == '<':
            count *= 5
            count += 4
            stack.pop()
            
    counts.append(count)
      

ans2 = sorted(counts)[int(len(counts)/2)]

print('answer1:', ans1)
print('answer2:', ans2)