file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia06/input.txt')
lst = file.readline()
cont = 0
for i in range(len(lst)):
    char_lst = set(lst[i:i+14])
    cont = i + 14
    if(len(char_lst) == 14):
        break

print(cont)