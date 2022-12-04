file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia04/input.txt')
lst = file.readlines()

overlap = 0
for pair in lst:
    pair = pair.split(',')
    first_pair = pair[0].split('-')
    second_pair = pair[1].split('-')
    if(int(second_pair[1]) - int(first_pair[1]) <= 0 and int(second_pair[0]) - int(first_pair[0]) >= 0):
        overlap += 1
    elif(int(first_pair[1]) - int(second_pair[1]) <= 0 and int(first_pair[0]) - int(second_pair[0]) >= 0):
        overlap += 1
print(overlap)