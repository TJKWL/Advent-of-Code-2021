data = open('data12.txt').read().splitlines()
final_data = []
for path in data:
    final_data.append(path.split('-'))

def find_new_cave(df, stacks, done_routes):
    new_stacks = []
    for route in stacks:
        for i in range(len(df)):
            char2 = ''
            new_route = route.copy()
            
            if df[i][0] == route[-1]:
                char2 = df[i][1]
            elif df[i][1] == route[-1]:
                char2 = df[i][0]
            if char2 != '':
                route_trial = new_route.copy()
                if char2 not in route:
                    new_route.append(char2)
                    new_stacks.append(new_route)
                elif char2.isupper():
                    new_route.append(char2)
                    new_stacks.append(new_route)
                else:
                    for char in route_trial:
                        if char.isupper():
                            route_trial.remove(char)
                    if len(route_trial) == len(set(route_trial)) and char2 != 'start' and char2 != 'end':
                        new_route.append(char2)
                        new_stacks.append(new_route)                                               
            if char2 == 'end':
                done_routes.append(new_route)
                new_stacks.remove(new_route)    
    if stacks == new_stacks:
        print('DONE')
        new_stacks = []        
    return new_stacks, done_routes
                    
done_routes = []
stacks = [['start']]

while len(stacks) != 0:
    [stacks, done_routes] = find_new_cave(final_data, stacks, done_routes)
    
print(len(done_routes))