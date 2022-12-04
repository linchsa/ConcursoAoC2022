file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia04/input.txt')
lst = file.readlines()
overlap = 0
for pair in lst:
    pair = pair.split(',')
    first_pair = pair[0].split('-')
    second_pair = pair[1].split('-')
    if(not (int(second_pair[0]) - int(first_pair[1]) > 0 or int(second_pair[1]) - int(first_pair[0]) < 0)):
        overlap += 1
    elif(not ( int(first_pair[0]) - int(second_pair[1]) > 0 or int(first_pair[1]) - int(second_pair[0]) < 0)):
        overlap += 1
print(overlap)