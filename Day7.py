data = open('data7.txt').read().split(',')
df = sorted([int(s) for s in data])
print(int(sum([abs(s - 0.5 * ( df[int(len(df)/2)]+ df[int(len(df)/2) - 1] )) for s in df])))
print(sum([int(n*(n+1)/2) for n in [abs(s-round(sum(df) / (len(df) + 1))) for s in df]]))