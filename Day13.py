data = open('data13.txt').read().splitlines()

char = data[-1]
folds = []
while char != '':
    folds.append(data[-1].split(' ')[-1])
    data.pop()
    char = data[-1]
    
data.pop()
folds.reverse()
new_folds = []

for fold in folds:
    new_folds.append(fold.split('='))
    
folds = new_folds

points = set()

for point in data:
    new_point = point.split(',')
    points.add((int(new_point[0]), int(new_point[-1])))

def do_a_fold(df, fold):
    new_data = set()
    if fold[0] == 'x':
        for point in df:
            if point[0] > int(fold[-1]):
                new_data.add((2*int(fold[-1]) - point[0], point[1]))
            else:
                new_data.add(point)
    elif fold[0] == 'y':
        for point in df:
            if point[1] > int(fold[-1]):
                new_data.add((point[0], 2*int(fold[-1]) - point[1]))
            else:
                new_data.add(point)               
    return new_data

for fold in folds:
    points = do_a_fold(points, fold)
    print(len(points))

##printing the final answer

indicator = [[' ' for x in range(39)] for y in range(6)]

for point in points:
    indicator[point[1]][point[0]] = '#'
    
for row in indicator:
    print(row)