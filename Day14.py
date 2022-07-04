data = open('data14.txt').read().splitlines()

chain = data[0]
data.remove(data[0])
data.remove(data[0])
final_chain = list(chain)

final_data = []

for interaction in data:
    final_data.append(interaction.split(' -> '))

indicator = [0 for x in range(len(final_data))]

for i in range(len(final_chain) - 1 ):
    for j in range(len(final_data)):
        if final_chain[i] == final_data[j][0][0] and final_chain[i+1] == final_data[j][0][1]:
            indicator[j] += 1

def do_one_pass(ind, df):
    new_indicator = [0 for x in range(len(indicator))]
    for i in range(len(indicator)):
        if indicator[i] > 0:
            n = indicator[i]
            new_letter = df[i][1][0]
            for j in range(len(df)):
                if df[j][0][0] == df[i][0][0] and df[j][0][1] == new_letter:
                    new_indicator[j] += n * 1
                if df[j][0][0] == new_letter and df[j][0][1] == df[i][0][1]:
                    new_indicator[j] += n * 1                    
    return new_indicator
            
def evaluate_ind(ind, df):
    display = set()
    for i in range(len(ind)):
        display.add(df[i][0][0])
    letters = list(display)
    amounts = [0 for x in range(len(letters))]
    for i in range(len(ind)):
        for j in range(len(display)):
            if letters[j] == df[i][0][0]:
               amounts[j] += ind[i]
    return sorted([[amounts[i],letters[i]] for i in range(len(letters))])
                
for i in range(40):
    indicator = do_one_pass(indicator, final_data)
    
print(evaluate_ind(indicator, final_data))
            
            


    
    
    