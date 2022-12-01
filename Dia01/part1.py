file = open('C:/Users/diego/OneDrive/Escritorio/VSCODE/ConcursoAoC2022/Dia01/input.txt')
lst = file.readlines()
print(lst)
current = 0
max = 0

for i in lst:
    if(i == '\n'):
        if(current >= max):
            max = current
            current = 0
        current = 0
    else:
        current += int(i)

print(max)